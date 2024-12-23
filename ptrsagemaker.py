# Python commandset for using sagemaker to utilise PTR data

import os
import glob
import shutil
import traceback
import getpass
import platform

# Make doubly sure these tempfiles aren't lying around.
try:
    os.remove('ldtk.py')
except:
    pass

try:
    os.remove('ldtk.doot')
except:
    pass

try:
    os.remove('client.py')
except:
    pass

try:
    os.remove('client.doot')
except:
    pass

try:
    os.remove('../ldtk.py')
except:
    pass

try:
    os.remove('../ldtk.doot')
except:
    pass

try:
    os.remove('../client.py')
except:
    pass

try:
    os.remove('../client.doot')
except:
    pass

try:
    os.remove('ptrsagemaker/ldtk.py')
except:
    pass

try:
    os.remove('ptrsagemaker/ldtk.doot')
except:
    pass

try:
    os.remove('ptrsagemaker/client.py')
except:
    pass

try:
    os.remove('ptrsagemaker/client.doot')
except:
    pass



try:
    import numpy
except:
    os.system('pip install -U numpy==1.26.4')
    import numpy
    
try:
    import wget
except:
    os.system('pip install wget')
    import wget

    
# try:
#     import bokeh
# except:
#     os.system('pip install bokeh')
#     import bokeh

try:
    from PIL import Image, ImageFont, ImageDraw
except:
    os.system('pip install pillow')
    from PIL import Image, ImageFont, ImageDraw

import json
import sys
try:
    from astropy.io import fits
except:
    os.system('pip install astropy~=6.1')
    #import astropy
    from astropy.io import fits




from pathlib import Path

try:
    import requests
    from requests.adapters import HTTPAdapter
    from requests.packages.urllib3.util.retry import Retry
except:
    os.system('pip install requests')
    import requests
    from requests.adapters import HTTPAdapter
    from requests.packages.urllib3.util.retry import Retry


#### CREATE EXOTIC LDTK DIRECTORY


homedir=os.path.expanduser('~')

if not os.path.exists(homedir+'/ldtables/'):
    os.makedirs(homedir+'/ldtables/')
if not os.path.exists(homedir+'/ldtables/Z+0.5'):
    os.makedirs(homedir+'/ldtables/Z+0.5')
if not os.path.exists(homedir+'/ldtables/Z+1.0'):
    os.makedirs(homedir+'/ldtables/Z+1.0')
if not os.path.exists(homedir+'/ldtables/Z-0.0'):
    os.makedirs(homedir+'/ldtables/Z-0.0')
if not os.path.exists(homedir+'/ldtables/Z-0.5'):
    os.makedirs(homedir+'/ldtables/Z-0.5')
if not os.path.exists(homedir+'/ldtables/Z-1.0'):
    os.makedirs(homedir+'/ldtables/Z-1.0')
if not os.path.exists(homedir+'/ldtables/Z-1.5'):
    os.makedirs(homedir+'/ldtables/Z-1.5')
if not os.path.exists(homedir+'/ldtables/Z-2.0'):
    os.makedirs(homedir+'/ldtables/Z-2.0')
if not os.path.exists(homedir+'/ldtables/Z-3.0'):
    os.makedirs(homedir+'/ldtables/Z-3.0')
if not os.path.exists(homedir+'/ldtables/Z-4.0'):
    os.makedirs(homedir+'/ldtables/Z-4.0')



try:
    import astrosource
    from astrosource import TimeSeries
    from astrosource.utils import get_targets, folder_setup, AstrosourceException, cleanup, convert_coords
except:
    os.system('pip install astrosource')
    os.system('pip3 install astrosource')
    os.system('pip install git+https://github.com/zemogle/astrosource@dev')
    os.system('pip3 install git+https://github.com/zemogle/astrosource@dev')
    os.system('pip install tqdm')
    os.system('pip3 install tqdm')
    import astrosource
    from astrosource import TimeSeries
    from astrosource.utils import get_targets, folder_setup, AstrosourceException, cleanup, convert_coords
    import tqdm

try:
    import numba
except:
    os.system('pip install -U numba')
    import numba


if platform.system() == "Windows":
    print ("Not loading exotic as not working in windows yet")
else:

    try:
        try:
            import exotic
            from exotic.exotic import NASAExoplanetArchive, get_wcs, find_target
        except:
            os.system('pip install exotic')
            os.system('pip install --upgrade setuptools')
            os.system('pip install git+https://github.com/mfitzasp/ptrEXOTIC@main')
            import exotic
            from exotic.exotic import NASAExoplanetArchive, get_wcs, find_target
            # Need to patch over the limb darkening tables as the default tries to link to an ftp server that blocks AWS for some reason
            #wget.download('https://www.solarsiblings.com/ldtables/ldtk.py', out='~/.conda/envs/default/lib/python3.9/site-packages/ldtk/ldtk.py')
            #def link_ldtk_to_oss():
    except:
        print ("EXOTIC IMPORT FAILED")
        print(traceback.format_exc())
            
if str(getpass.getuser()) == 'studio-lab-user':
    try:
        if not os.path.exists('~/.conda/envs/default/lib/python3.9/site-packages/ldtk/ldtk.doot'):
            wget.download('https://www.oursolarsiblings.com/ldtk.doot')
            if not os.path.exists('~/.conda/envs/default/lib/python3.9/site-packages/ldtk/ldtk.doot'):
                os.system('cp ldtk.doot ~/.conda/envs/default/lib/python3.9/site-packages/ldtk/ldtk.doot')
            os.rename('ldtk.doot','ldtk.py')
            try:
                os.system('mv ldtk.py ~/.conda/envs/default/lib/python3.9/site-packages/ldtk/ldtk.py')
            except:
                try:
                    os.remove('ldtk.py')
                except:
                    pass
                
                try:
                    os.remove('ldtk.doot')
                except:
                    pass
            
            wget.download('https://www.oursolarsiblings.com/client.doot')
            os.rename('client.doot','client.py')
            try:
                os.system('mv client.py ~/.conda/envs/default/lib/python3.9/site-packages/ldtk/client.py')
            except:
                try:
                    os.remove('client.py')
                except:
                    pass
                
                try:
                    os.remove('client.doot')
                except:
                    pass
    except:
        print ("SOMETHING FAILED IN THE LDTK update")    
        print(traceback.format_exc())



print ("********************")
print ("PTRSAGEMAKER LOADED")
print ("********************")

def update_packages():
    os.system('pip install -U tqdm')
    os.system('pip uninstall -y astrosource')
    os.system('pip install -U git+https://github.com/zemogle/astrosource@dev')
    os.system('pip install -U requests')
    os.system('pip install -U wget')
    
    os.system('pip install -U numpy==1.26.4')
    os.system('pip install -U scipy')
    os.system('pip install -U setuptools')
    os.system('pip install git+https://github.com/mfitzasp/ptrEXOTIC@main')
    
    os.system('pip install -U astropy~=6.1')
    print ("Packages updated. Please restart your console to use the latest packages.")
    

def list_commands():
    print ("analysis commands")
    print ("******************")
    print ("download_frames_from_ptrarchive")
    print ("run_astrosource_on_photfiles")
    print ("remove_smartstacks_from_directory")
    print ("\nnavigation commands")
    print ("******************")
    print ("where_am_i")
    print ("\nsystem commands")
    print ("******************")
    print ("update_packages")

    
def where_am_i():
    print (os.cwd())
    

def download_wasp43_sampledata():
    wget.download('https://www.oursolarsiblings.com/wasp43b_sampledata.zip')
    if not os.path.exists('waspsample'):
        os.makedirs('waspsample')
    #shutil.move('wasp43b_sea.zip','waspsample/wasp43b_sea.zip')
    shutil.unpack_archive('wasp43b_sampledata.zip', 'waspsample')
    
    wget.download('http://www.oursolarsiblings.com/lsc0m412-kb26-20180222-0358-e91.fits')
    shutil.move('lsc0m412-kb26-20180222-0358-e91.fits', 'waspsample')
    
    
def test_run_exotic_on_wasp_data():
    
    # Create inits file from fits file
    if not os.path.exists('waspsample/init.json'):
        form_exotic_init_file_from_fits_files(directory='waspsample', init_filename='waspsample/init.json')
    
    # Run astrosource to get transit observation
    if not os.path.exists('waspsample/outputcats/V1_calibEXOTIC.csv'):
        run_astrosource_on_photfiles('waspsample', ra=154.9083708,dec=-9.8062778, format='sea', period=False, calib=False)
    
    # Then run EXOTIC on resulting files
    run_exotic_on_prereduced_files('waspsample/outputcats/V1_diffEXOTIC.csv', 'waspsample/init.json', check_exoarchive_values=False)
    
    
def run_exotic_on_phot_files(directory, ra=0.0, dec=0.0, photformat='psx'):

    #print ('yay')    
    
    if not os.path.exists(directory + '/init.json'):
        form_exotic_init_file_from_fits_files(directory=directory, init_filename=directory + '/init.json')
        
    # Run astrosource to get transit observation
    if not os.path.exists(directory +'/outputcats/V1_calibEXOTIC.csv'):
        run_astrosource_on_photfiles(directory, ra=ra,dec=dec, format=photformat, period=False, calib=False)
        
    # Then run EXOTIC on resulting files
    run_exotic_on_prereduced_files(directory +'/outputcats/V1_diffEXOTIC.csv', directory +'/init.json', check_exoarchive_values=False)
    


def link_ldtk_to_oss():
    if str(getpass.getuser()) == 'studio-lab-user':
        wget.download('https://www.oursolarsiblings.com/ldtk.doot')
        if not os.path.exists('~/.conda/envs/default/lib/python3.9/site-packages/ldtk/ldtk.doot'):
            os.system('cp ldtk.doot ~/.conda/envs/default/lib/python3.9/site-packages/ldtk/ldtk.doot')
        os.rename('ldtk.doot','ldtk.py')
        os.system('mv ldtk.py ~/.conda/envs/default/lib/python3.9/site-packages/ldtk/ldtk.py')
        
        wget.download('https://www.oursolarsiblings.com/client.doot')
        os.rename('client.doot','client.py')
        os.system('mv client.py ~/.conda/envs/default/lib/python3.9/site-packages/ldtk/client.py')
        

def remove_smartstacks_from_directory(directory):
    files = glob.glob(directory + '/*SmSTACK*')
    for f in files:
        try:
            print ("Removing: " + str(f))
            os.remove(f)
        except:
            pass    
    print ("Finished removing smartstacks")

def remove_nonsmartstacks_from_directory(directory, format='sek'):
    files = glob.glob(directory + '/*.' + str(format))
    for f in files:
        if 'SmSTACK' not in f:
            print ("Removing nonsmartstack: " + str(f))
            try:                
                os.remove(f)
            except:
                pass    
    print ("Finished removing non-smartstacks")
        
# ptrsagemaker.remove_mispointed_frames('googy',295.2075,-27.6949,2)
def remove_mispointed_frames(directory,ra,dec,radius, format='sek'):
    files=glob.glob(directory + '/*.'+format)
    #print (files)
    for file in files:
        templist=numpy.genfromtxt(file, dtype=float, delimiter=',')
        print ("Checking " + str(file) + " ......")
        fileRA=numpy.nanmedian(templist[:,0])
        fileDEC=numpy.nanmedian(templist[:,1])
        del templist
        if abs(ra-fileRA) > radius:
            print ("Too far in RA! Rejecting this one")
            try:
                print ("Removing: " + str(file))
                os.remove(file)
            except:
                pass
        elif abs(dec-fileDEC) > radius:
            print ("Too far in DEC! Rejecting this one")
            try:
                print ("Removing: " + str(file))
                os.remove(file)
            except:
                pass
    print ("Removing mispointed frames completed.")

def zip_folder(directory):
    shutil.make_archive(directory + '.zip', 'zip', directory)
    print ("Zipped " + str(directory))
    

def list_file_sizes(directory, format='sek'):
    files=glob.glob(directory + '/*.'+format)
    for file in files:
        print (file)
        file_stats = os.stat(file)
        #print(file_stats)
        print(f'File Size in KiloBytes is {file_stats.st_size / (1024)}')

def remove_small_filesizes(directory, smallest_size, format='sek'):
    files=glob.glob(directory + '/*.'+format)
    for file in files:
        #print (file)
        file_stats = os.stat(file)
        #print(file_stats)
        if (file_stats.st_size / (1024)) < smallest_size:
            print (file + " removed for being too small")
            print(f'File Size in KiloBytes is {file_stats.st_size / (1024)}')
            try:
                print ("Removing: " + str(file))
                os.remove(file)
            except:
                pass


def download_frames_from_ptrarchive(location='.', frames=[]):
    
    
    session = requests.Session()
    retry = Retry(connect=5, backoff_factor=2.0, allowed_methods=frozenset(['GET', 'POST']))
    #retry = Retry(connect=5, backoff_factor=2.0)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    
    #frames='(509954,507152,509116,507858,508370,508106,510918,509917,508897,508196,507674,507629,507970,510577,510612,507818,508289,509879,507344,507890,509137,510364,508233,507389,508701,507714,508178,508138,507637,508114,508307,507994,507605,510686,507210,507597,507698,510591,509082,509458,509014,510768,508082,507224,507423,508668,507668,507954,509968,510161,507738,510125,510413,507730,507312,508273,508623,507866,509000,508034,507778,508881,509063,510472,509683,507328,508968,508800,508313,507469,508910,508759,508653,509651,508281,509425,508130,507908,508074,507240,510854,509514)'
    
    
    authtoken="AUTHTOKEN"
    frame_url="https://archiveapi.photonranch.org/frames/"
    frames=frames.replace('(','').replace(')','')
    frames=frames.split(',')
    
    if not os.path.exists(location):
        os.makedirs(location)
        
    for frame in frames:
        response=session.get(frame_url + frame)
        download_url=response.json()['url']
        print ("Downloading: " + str(response.json()['filename']))
        with open(location + '/' + response.json()['filename'],'wb') as f:
            f.write(session.get(download_url).content)
        
    #breakpoint()
    
    print ("Download_frames_from_ptrarchive")



def create_pdf_of_images(requestedimages, outputname):
    
    
    fileList=glob.glob(requestedimages)
    images=[]
    for file in fileList:
        print ("Collecting: " + str(file))
        if 'png' in file:
            img=Image.open(file).convert("RGB")
        else:
            img=Image.open(file)
        
        Im = ImageDraw.Draw(img)
        Im.text((10, 10), file.split('/')[-1],fill=(0, 0, 0))
        images.append(img)        
    
    images[0].save(outputname, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])
        
    
    
    
    # img=Image.open(fileList[0])
    # if 'png' in fileList[0]:
    #     img=img.convert("RGB")
    # fileshowing=fileList[0]
    # index=0
    # opt='z'
    
    
    # images=[]
    # for file in fileList:
    #     print ("Collecting: " + str(file))
    #     if 'png' in file:
    #         images.append(Image.open(file).convert("RGB"))
    #     else:
    #         images.append(Image.open(file))
        
    # pdf_path = "googsplat.pdf"        
    
    # images[0].save(pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])
    
    
    
    # while True:
    #     #img.show()
    #     print ("File " +str(index+1) + " Showing: " + str(fileshowing))
    #     if index < len(fileList):
    #         index=index+1
    #         img=Image.open(fileList[index])
    #         if 'png' in fileList[index]:
    #             img=img.convert("RGB")
                
    #         fileshowing=fileList[index]
            
    
    
    
    
    # while opt != 'x':
    #     img.show()
    #     print ("File " +str(index+1) + " Showing: " + str(fileshowing))
    #     while opt != 'x':
    #         opt=input()
    #         if opt == 'n':
    #             if index < len(fileList):
    #                 index=index+1
    #                 img=Image.open(fileList[index])
    #                 if 'png' in fileList[index]:
    #                     img=img.convert("RGB")
    #                 fileshowing=fileList[index]
    #                 break
    #             else:
    #                 print ("reached end of list")
    #         elif opt == 'p':
    #             if index < len(fileList):
    #                 index=index+1
    #                 img=Image.open(fileList[index])
    #                 if 'png' in fileList[index]:
    #                     img=img.convert("RGB")
    #                 fileshowing=fileList[index]
    #                 break
    #             else:
    #                 print ("can't go past start of list")
    #         elif opt == 'x':        
    #             print ("cancelling out")
    #         else:
    #             print ("That was neither an n or a p or an x, try again")
        
                
                    
                
                




def run_astrosource_on_photfiles(indir, full=True, stars=True, comparison=True, variablehunt=False, notarget=False, lowestcounts=1800, usescreenedcomps=False, usepreviousvarsearch=False, \
    calibsave=False, outliererror=4, outlierstdev=4, varsearchglobalstdev=-99.9, varsearchstdev=2, varsearchmagwidth=0.5, \
    varsearchminimages=0.3, ignoreedgefraction=0.05, usecompsused=False, usecompletedcalib=False, mincompstarstotal=-99, calc=True, \
    calib=True, phot=True, plot=True, detrend=False, eebls=False, period=True, ra=None, dec=None, target_file=None, format='sek', imgreject=0.05, \
    mincompstars=0.1, maxcandidatestars=10000, closerejectd=5.0, bjd=True, clean=False, verbose=True, debug=False, periodlower=-99.9, periodupper=-99.9, \
    periodtests=10000,  thresholdcounts=1000000, nopanstarrs=False, nosdss=False, varsearch=False, varsearchthresh=10000, starreject=0.3, hicounts=3000000, \
    lowcounts=5000, colourdetect=False, linearise=False, colourterm=0.0, colourerror=0.0, targetcolour=-99.0, restrictmagbrightest=-99.9, \
    restrictmagdimmest=99.9, rejectmagbrightest=-99.9, rejectmagdimmest=99.9,targetradius=1.5, matchradius=1.0, racut=-99.9, deccut=-99.9, \
    radiuscut=-99.9, restrictcompcolourcentre=-99.9, restrictcompcolourrange=-99.9, detrendfraction=0.1, minfractionimages=0.5):
    parentPath='testphotfiles'
    
    
    #fileList=glob.glob(string_list)
    #indir='testphotfiles/'
    
    # Default options
    parentPath = Path(indir)
    if clean:
        cleanup(parentPath)
        print('All output files removed')
        return
    if not (ra and dec) and not target_file and not variablehunt:
        #logger.error("Either RA and Dec or a targetfile must be specified")
        print("No specified RA or Dec nor targetfile nor request for a variable hunt. It is assumed you have no target to analyse.")
        notarget=True
        #return



    if ra and dec:
        ra, dec = convert_coords(ra, dec)
        targets = numpy.array([(ra, dec, 0, 0)])
    elif target_file:
        target_file = parentPath / target_file
        targets = get_targets(target_file)
    elif notarget == True or variablehunt == True:
        targets = None

    if variablehunt == True:
        varsearch=True
        full=True


    if usecompletedcalib == True:
        usecompsused = True

    if usecompsused == True:
        usescreenedcomps = True
    
    #from astrosource import TimeSeries
    ts = astrosource.TimeSeries(indir=parentPath,
                        targets=targets,
                        format=format,
                        imgreject=imgreject,
                        periodupper=periodupper,
                        periodlower=periodlower,
                        periodtests=periodtests,
                        thresholdcounts=thresholdcounts,
                        lowcounts=lowcounts,
                        hicounts=hicounts,
                        starreject=starreject,
                        nopanstarrs=nopanstarrs,
                        nosdss=nosdss,
                        closerejectd=closerejectd,
                        maxcandidatestars=maxcandidatestars,
                        verbose=verbose,
                        debug=debug,
                        bjd=bjd,
                        mincompstars=mincompstars,
                        mincompstarstotal=mincompstarstotal,
                        colourdetect=colourdetect,
                        linearise=linearise,
                        variablehunt=variablehunt,
                        calibsave=calibsave,
                        notarget=notarget,
                        usescreenedcomps=usescreenedcomps,
                        usepreviousvarsearch=usepreviousvarsearch,
                        colourterm=colourterm,
                        colourerror=colourerror,
                        targetcolour=targetcolour,
                        restrictmagbrightest=restrictmagbrightest,
                        restrictmagdimmest=restrictmagdimmest,
                        rejectmagbrightest=rejectmagbrightest,
                        rejectmagdimmest=rejectmagdimmest,
                        targetradius=targetradius,
                        matchradius=matchradius,
                        varsearchglobalstdev=varsearchglobalstdev,
                        varsearchthresh=varsearchthresh,
                        varsearchstdev=varsearchstdev,
                        varsearchmagwidth=varsearchmagwidth,
                        varsearchminimages=varsearchminimages,
                        ignoreedgefraction=ignoreedgefraction,
                        outliererror=outliererror,
                        outlierstdev=outlierstdev,
                        lowestcounts=lowestcounts,
                        racut=racut,
                        deccut=deccut,
                        radiuscut=radiuscut,
                        restrictcompcolourcentre=restrictcompcolourcentre,
                        restrictcompcolourrange=restrictcompcolourrange,
                        detrendfraction=detrendfraction,
                        minfractionimages=minfractionimages
                        )
    
    if full or comparison:
        ts.analyse(usescreenedcomps=usescreenedcomps, usecompsused=usecompsused, usecompletedcalib=usecompletedcalib, calib=calib)


    if (full or calc) and varsearch and not usepreviousvarsearch :
        ts.find_variables()

    if variablehunt == True:
        targets = get_targets(parentPath / 'results/potentialVariables.csv')



    if targets is not None:
        if full or phot:
            ts.photometry(filesave=True, targets=targets)
        if full or plot:
            ts.plot(detrend=detrend, period=period, eebls=eebls, filesave=True)

    print("✅ AstroSource analysis complete\n")

#download_frames_from_ptrarchive()

def run_exotic_on_prereduced_files(prereduced_filename, inits_filename, check_exoarchive_values):
    import exotic.exotic
    exotic.exotic.main(prereduced=True, prereduced_filename=prereduced_filename, inits_filename=inits_filename, check_exoarchive_values=check_exoarchive_values)


def run_exotic_on_fits_files(directory=None):
    print ("Run exotic on fits files")
    
def run_astrosource_on_fits_files_then_exotic(directory=None):
    print ("Run astrosource then exotic on fits files")
    
def form_exotic_init_file_from_fits_files(directory=None, init_filename='init.json'):    
    print ("forming exotic inits file from fits files.")
    files = glob.glob(directory + '/*.f*')
    
    #Open the first file to get info
    hduhold =fits.open(files[0])[0]
    header=hduhold.header
    
        
    
    period_days=""
    while period_days=="":
        print ("Orbital Period (days). This is NEEDED.")
        period_days=input()
    print ("Orbital Period Uncertainty. (Press ENTER if you do not know)")    
    period_uncertainty=input()
    if period_uncertainty == "":
        period_uncertainty = 0.001        
    elif float(period_uncertainty) < 0.001:
        period_uncertainty = 0.001
    
    published_mid_transit=""
    while published_mid_transit=="":
        print ("Published Mid-Transit Time (BJD-UTC preferred or JD or HJD). This is NEEDED.")
        published_mid_transit=input()
    print ("Mid-Transit Time Uncertainty. (Press ENTER if you do not know)")
    published_mid_transit_unc=input()
    if published_mid_transit_unc == "":
        published_mid_transit_unc = 0.001
    elif float(published_mid_transit_unc) < 0.001:
        published_mid_transit_unc = 0.001
    print ("Ratio of Planet to Stellar Radius (Rp/Rs). (Press ENTER if you do not know)")
    rp_to_rs=input()
    if rp_to_rs == "":
        rp_to_rs = 0.15
    print ("Ratio of Planet to Stellar Radius (Rp/Rs) Uncertainty. (Press ENTER if you do not know)")
    rp_to_rs_unc=input()
    if rp_to_rs_unc == "":
        rp_to_rs_unc = 0.125
    if float(rp_to_rs_unc) < 0.1:
        rp_to_rs_unc = 0.1
    print ("Ratio of Distance to Stellar Radius (a/Rs). (Press ENTER if you do not know)")
    a_to_rs=input()
    if a_to_rs == "":
        a_to_rs = 20
    print ("Ratio of Distance to Stellar Radius (a/Rs) Uncertainty. (Press ENTER if you do not know)")
    a_to_rs_unc=input()
    if a_to_rs_unc == "":
        a_to_rs_unc = 15
    if float(a_to_rs_unc) < 0.1:
        a_to_rs_unc = 0.1
    print ("Orbital Inclination (deg). (Press ENTER if you do not know)")
    inclination=input()
    if inclination == "":
        inclination = 85
    
    print ("Orbital Inclination (deg) Uncertainty. (Press ENTER if you do not know)")
    inclination_unc=input()
    if inclination_unc == "":
        inclination_unc = 20
    if float(inclination_unc) < 5:
        inclination_unc = 5
    print ("Orbital Eccentricity (0 if null). (Press ENTER if you do not know)")
    eccentricity=input()
    if eccentricity == "":
        eccentricity = 0
    print ("Argument of Periastron (deg). (Press ENTER if you do not know)")
    arg_periastron=input()
    if arg_periastron == "":
        arg_periastron = 0
    print ("Star Effective Temperature (K). (Press ENTER if you do not know)")
    star_eff_temp=input()
    if star_eff_temp == "":
        star_eff_temp = 5500
    print ("Star Effective Temperature (+) Uncertainty. (Press ENTER if you do not know)")
    star_eff_temp_plusunc=input()
    if star_eff_temp_plusunc == "":
        star_eff_temp_plusunc = 200
    print ("Star Effective Temperature (-) Uncertainty. (Press ENTER if you do not know)")
    star_eff_temp_minusunc=input()
    if star_eff_temp_minusunc == "":
        star_eff_temp_minusunc = 200
    print ("Star Metallicity ([FE/H]). (Press ENTER if you do not know)")
    star_metal=input()
    if star_metal == "":
        star_metal = 0.0
    print ("Star Metallicity (+) Uncertainty. (Press ENTER if you do not know)")
    star_metal_plusunc=input()
    if star_metal_plusunc == "":
        star_metal_plusunc = 0.5
    print ("Star Metallicity (-) Uncertainty. (Press ENTER if you do not know)")
    star_metal_minusunc=input()
    if star_metal_minusunc == "":
        star_metal_minusunc = 0.5
    print ("Star Surface Gravity (log(g)). (Press ENTER if you do not know)")
    star_logg=input()
    if star_logg == "":
        star_logg = 4.5
    print ("Star Surface Gravity (+) Uncertainty. (Press ENTER if you do not know)")
    star_logg_plusunc=input()
    if star_logg_plusunc == "":
        star_logg_plusunc = 0.5
    print ("Star Surface Gravity (-) Uncertainty. (Press ENTER if you do not know)")
    star_logg_minusunc=input()
    if star_logg_minusunc == "":
        star_logg_minusunc = 0.5
    
    try:
        tempRAin= header['RA-HMS']
        tempDECin= header['DEC-DMS']
    except:
        tempRAin= header['RA']
        tempDECin= header['DEC']
    
    
    inits_file={
            "inits_guide": {
            "Title": "EXOTIC's Initialization File",
            "Comment": "Please answer all the following requirements below by following the format of the given",
            "Comment1": "sample dataset HAT-P-32 b. Edit this file as needed to match the data wanting to be reduced.",
            "Comment2": "Do not delete areas where there are quotation marks, commas, and brackets.",
            "Comment3": "The inits_guide dictionary (these lines of text) does not have to be edited",
            "Comment4": "and is only here to serve as a guide. Will be updated per user's advice.",
            "Image Calibrations Directory Guide": "Enter in the path to image calibrations or enter in null for none.",
            "Planetary Parameters Guide": "For planetary parameters that are not filled in, enter in null.",
            "Comparison Star(s) Guide": "Up to 10 comparison stars can be added following the format given below.",
            "Obs. Latitude Guide": "Indicate the sign (+ North, - South) before the degrees. Needs to be in decimal or HH:MM:SS format.",
            "Obs. Longitude Guide": "Indicate the sign (+ East, - West) before the degrees. Needs to be in decimal or HH:MM:SS format.",
            "Camera Type (1)": "If you are using a CMOS, please enter CCD in 'Camera Type (CCD or DSLR)' and then note",
            "Camera Type (2)": "your actual camera type under 'Observing Notes'.",
            "Plate Solution": "For your image to be given a plate solution, type y.",
            "Plate Solution Disclaimer": "One of your imaging files will be publicly viewable on nova.astrometry.net.",
            "Standard Filter": "To use EXOTIC standard filters, type only the filter name.",
            "Custom Filter": "To use a custom filter, enter in the FWHM in optional_info.",
            "Target Star RA": "Must be in HH:MM:SS sexagesimal format.",
            "Target Star DEC": "Must be in +/-DD:MM:SS sexagesimal format with correct sign at the beginning (+ or -).",
            "Demosaic Format": "Optional control for handling Bayer pattern color images - to use, provide Bayer color patttern of your camera (RGGB, BGGR, GRBG, GBRG) - null (no color processing) is default",
            "Demosaic Output": "Select how to process color data (gray for grayscale, red or green or blue for single color channel, blueblock for grayscale without blue, [ R, G, B ] for custom weights for mixing colors.  green is default",
            "Formatting of null": "Due to the file being a .json, null is case sensitive and must be spelled as shown.",
            "Decimal Format": "Leading zero must be included when appropriate (Ex: 0.32, .32 or 00.32 causes errors.)."
    },
    "user_info": {
            "Directory with FITS files": str(directory),
            "Directory to Save Plots": str(directory),
            "Directory of Flats": 'null',
            "Directory of Darks": 'null',
            "Directory of Biases": 'null',

            "AAVSO Observer Code (blank if none)": "",
            "Secondary Observer Codes (blank if none)": "",

            "Observation date": header['DAY-OBS'],
            "Obs. Latitude": ('+'+str(header['LATITUDE'])).replace('+-','-'),
            "Obs. Longitude": ('+'+str(header['LONGITUD'])).replace('+-','-'),
            "Obs. Elevation (meters)": header['HEIGHT'],
            "Camera Type (CCD or DSLR)": "CCD",
            "Pixel Binning": "1x1",
            "Filter Name (aavso.org/filters)": header['FILTER'],
            "Observing Notes": "",

            "Plate Solution? (y/n)": "y",
            "Add Comparison Stars from AAVSO? (y/n)": "y",

            "Target Star X & Y Pixel": "[424, 286]",
            "Comparison Star(s) X & Y Pixel": "[[465, 183], [512, 263], [], [], [], [], [], [], [], []]",

            "Demosaic Format": 'null',
            "Demosaic Output": 'null'
    },        
    
    
    "planetary_parameters": {
            "Target Star RA": tempRAin,
            "Target Star Dec": tempDECin,
            "Planet Name": header['OBJECT'],
            "Host Star Name": header['OBJECT'],
            "Orbital Period (days)": float(period_days),
            "Orbital Period Uncertainty": float(period_uncertainty),
            "Published Mid-Transit Time (BJD-UTC)": float(published_mid_transit),
            "Mid-Transit Time Uncertainty": float(published_mid_transit_unc),
            "Ratio of Planet to Stellar Radius (Rp/Rs)": float(rp_to_rs),
            "Ratio of Planet to Stellar Radius (Rp/Rs) Uncertainty": float(rp_to_rs_unc),
            "Ratio of Distance to Stellar Radius (a/Rs)": float(a_to_rs),
            "Ratio of Distance to Stellar Radius (a/Rs) Uncertainty": float(a_to_rs_unc),
            "Orbital Inclination (deg)": float(inclination),
            "Orbital Inclination (deg) Uncertainty": float(inclination_unc),
            "Orbital Eccentricity (0 if null)": float(eccentricity),
            "Argument of Periastron (deg)": float(arg_periastron),
            "Star Effective Temperature (K)": float(star_eff_temp),
            "Star Effective Temperature (+) Uncertainty": float(star_eff_temp_plusunc),
            "Star Effective Temperature (-) Uncertainty": float(star_eff_temp_minusunc),
            "Star Metallicity ([FE/H])": float(star_metal),
            "Star Metallicity (+) Uncertainty": float(star_metal_plusunc),
            "Star Metallicity (-) Uncertainty": float(star_metal_minusunc),
            "Star Surface Gravity (log(g))": float(star_logg),
            "Star Surface Gravity (+) Uncertainty": float(star_logg_plusunc),
            "Star Surface Gravity (-) Uncertainty": float(star_logg_minusunc)
    },
    "optional_info": {
            "Pre-reduced File:": "",
            "Pre-reduced File Time Format (BJD_TDB, JD_UTC, MJD_UTC)": "BJD_TDB",
            "Pre-reduced File Units of Flux (flux, magnitude, millimagnitude)": "flux",

            "Filter Minimum Wavelength (nm)": 'null',
            "Filter Maximum Wavelength (nm)": 'null',

            "Image Scale (Ex: 5.21 arcsecs/pixel)": float(header['PIXSCALE']),

            "Exposure Time (s)": float(header['EXPTIME'])
        
    }
        
        
    
        
        
        
        }
    # Store the JSON data in a file
    with open(init_filename, "w") as file:
        #json.dump(data, file)
        json.dump(inits_file, file)
    
    print ("inits file written.")
    #breakpoint()
    
    
    
# from ptrsagemaker import ptrsagemaker
# ptrsagemaker.form_exotic_init_file_from_fits_files(directory='tristantoi')

#breakpoint()
    
#run_astrosource_on_photfiles()