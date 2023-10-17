# ptr-sagemaker
 PTR commands for sagemaker

# Clone Instruction set
 https://github.com/mfitzasp/ptrsagemaker

# Initialise Instructions

 from ptrsagemaker import prtsagemaker

# Commands

 Download files:
 
ptrsagemaker.download_frames_from_ptrarchive(location='Folder name', frames='Insert frame numbers, separated, by comma')

 Run astrosource:

ptrsagemaker.run_astrosource_on_photfiles('Folder name')

ptrsagemaker.run_astrosource_on_photfiles('Folder name', ra='RA in decimal', dec='DEC in decimal')