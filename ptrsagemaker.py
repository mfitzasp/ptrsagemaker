# Python commandset for using sagemaker to utilise PTR data

import os
import glob
import shutil

try:
    import numpy
except:
    os.system('pip install numpy')
    import numpy
    
try:
    import wget
except:
    os.system('pip install wget')
    import wget
import json
import sys
try:

    from astropy.io import fits
except:
    os.system('pip install astropy')
    import astropy
    
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

try:
    import astrosource
    from astrosource import TimeSeries
    from astrosource.utils import get_targets, folder_setup, AstrosourceException, cleanup, convert_coords
except:
    os.system('pip install git+https://github.com/zemogle/astrosource@dev')
    os.system('pip install tqdm')
    import astrosource
    from astrosource import TimeSeries
    from astrosource.utils import get_targets, folder_setup, AstrosourceException, cleanup, convert_coords
    import tqdm

def update_packages():
    os.system('pip install -U tqdm')
    os.system('pip uninstall -y astrosource')
    os.system('pip install -U git+https://github.com/zemogle/astrosource@dev')
    os.system('pip install -U requests')
    os.system('pip install -U wget')
    os.system('pip install -U astropy')
    os.system('pip install -U numpy')
    print ("Packages updated. Please restart your console to use the latest packages.")
    

def list_commands():
    print ("analysis commands")
    print ("******************")
    print ("download_frames_from_ptrarchive")
    print ("run_astrosource_on_photfiles")
    print ("\nnavigation commands")
    print ("******************")
    print ("where_am_i")
    print ("\nsystem commands")
    print ("******************")
    print ("update_packages")

    
def where_am_i():
    print (os.cwd())
    

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
        
    breakpoint()
    
    print ("Download_frames_from_ptrarchive")

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
        ts.analyse(usescreenedcomps=usescreenedcomps, usecompsused=usecompsused, usecompletedcalib=usecompletedcalib)


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

breakpoint()
    
#run_astrosource_on_photfiles()