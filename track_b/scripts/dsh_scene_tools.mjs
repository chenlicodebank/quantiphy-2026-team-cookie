const { defineTool } = await import(process.env.QP_DSH_TOOLS_MODULE);
export const name = 'quantiphy-scene-sam3-tools';
export const inject = ['tools', 'attachments'];
// dsh_scene.py --sam3-url (method_queue 54, 2026-10-22): dsh_coder_tools.mjs plus SAM 3 segment / track, served by
// scripts/sam3_server.py through the Python bridge (QP_DSH_BRIDGE). Every call is executed by the bridge.
export function apply(ctx) {
  for (const tool of [
    {name:'video_frames',description:'View the video. mode=sheet: a contact sheet of n evenly spaced frames labelled with frame index and time. mode=frame: one frame at time t (seconds) or index i, optionally cropped to [x0,y0,x1,y1] in ORIGINAL pixels, enlarged by scale, with labelled grid lines every grid pixels. Coordinates you read stay original full-frame pixels.',parameters:{mode:{type:'string',enum:['sheet','frame'],required:true},n:{type:'integer'},t:{type:'number'},i:{type:'integer'},crop:{type:'array',items:{type:'number'}},scale:{type:'number'},grid:{type:'integer'}}},
    {name:'run_python',description:'Write a Python script into the workspace and run it there (numpy, scipy, opencv as cv2, PIL, av available; video.mp4 and inputs.json are in the working directory). Returns stdout/stderr (truncated) and the image files the script created. No network, no files outside the workspace, 240 s limit. Save any image you want to inspect (e.g. masks or points drawn on frames) and view it with view_image.',parameters:{filename:{type:'string',required:true},code:{type:'string',required:true}}},
    {name:'view_image',description:'Look at an image file (png/jpg) your code wrote inside the workspace, e.g. frames/overlay_12.png.',parameters:{path:{type:'string',required:true}}},
    {name:'segment',description:'SAM 3 (open weights) on one frame: every instance of a short noun phrase (e.g. "red car", "basketball", "wooden pier") at time t (seconds) or frame index i, numbered by score. Returns per instance its score, box [x0,y0,x1,y1], centroid, mask extents in full-resolution pixels (length_px along its main axis, width_px across it, axis_deg, horiz_px, vert_px), touches_border, and the saved mask file (masks/*.png, white = object) for your own scripts, plus an overlay image with the numbered outlines. Optional box [x0,y0,x1,y1] prompts SAM 3 with a box instead of (or with) the phrase.',parameters:{phrase:{type:'string',required:true},t:{type:'number'},i:{type:'integer'},box:{type:'array',items:{type:'number'}},max_instances:{type:'integer'}}},
    {name:'track',description:'SAM 3 video tracking of one phrase through the whole clip. Pass the frame index i and the box of the instance you mean (from segment) so the right object is followed. Writes tracks/*.csv (frame, t_file = frame / file fps, cx, cy, x0, y0, x1, y1, area, touches_border) and returns a linear pixel speed and a quadratic pixel acceleration fit, the other candidate instances, and an overlay of the track. every = frame step (default 1).',parameters:{phrase:{type:'string',required:true},i:{type:'integer'},box:{type:'array',items:{type:'number'}},k:{type:'integer'},every:{type:'integer'}}},
    {name:'finish_answers',description:'Finalize one positive number for EVERY question id, in the unit the question asks, with a short reason (method and the second-route check).',parameters:{answers:{type:'array',items:{type:'object',properties:{id:{type:'integer',required:true},value:{type:'number',required:true},reason:{type:'string',required:true}},additionalProperties:false},required:true}}}
  ]) ctx.tools.register(defineTool({...tool,output:{schema:{type:'json'},render:(_args,value)=>value.content},
    async execute(args,exec) {
      const r=await fetch(process.env.QP_DSH_BRIDGE+'/tool/'+tool.name,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(args),signal:exec.signal});
      if(!r.ok) throw new Error(await r.text());
      const data=await r.json();const content=[{type:'text',text:JSON.stringify(data.meta)}];
      for(const item of data.images||[]) {
        content.push({type:'text',text:JSON.stringify(item.meta)});
        const attachment=await ctx.attachments.saveImage({data:Buffer.from(item.image,'base64'),mediaType:'image/jpeg',name:'view.jpg'});
        content.push({type:'image',attachment});
      }
      return {content};
    }
  }));
}
