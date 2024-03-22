#!/usr/bin/env python3

import os
import shutil
import hashlib
import time
import re
import itertools
import threading
import sys
import ssl
import urllib.request
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from platform import python_version

################################################################
#
# Generated by: NCAR Climate Data Gateway
# Created: 2024-03-18T01:03:45-06:00
#
# Your download selection includes data that might be secured using API Token based
# authentication. Therefore, this script can have your api-token. If you
# re-generate your API Token after you download this script, the download will
# fail. If that happens, you can either re-download the script or you can edit
# this script replacing the old API Token with the new one. View your API token
# by going to "Account Home":
#
# https://www.earthsystemgrid.org/account/user/account-home.html
#
# and clicking on the "API Token" link under "Personal Account". You will be asked
# to log into the application before you can view your API Token.
#
# Usage: python3 python-ucar.cgd.cesm2le.atm.proc.monthly_ave.WSPDSRFAV-20240318T0103.py
# Version: 1.0.1
#
# Dataset
# ucar.cgd.cesm2le.atm.proc.monthly_ave.WSPDSRFAV
# 442f72c5-c347-4496-a490-f650ff6eba1b
# https://www.earthsystemgrid.org/dataset/ucar.cgd.cesm2le.atm.proc.monthly_ave.WSPDSRFAV.html
# https://www.earthsystemgrid.org/dataset/id/442f72c5-c347-4496-a490-f650ff6eba1b.html
#
# Dataset Version
# 2
# bda01a38-d22c-4b40-b106-687d066a072d
# https://www.earthsystemgrid.org/dataset/ucar.cgd.cesm2le.atm.proc.monthly_ave.WSPDSRFAV/version/2.html
# https://www.earthsystemgrid.org/dataset/version/id/bda01a38-d22c-4b40-b106-687d066a072d.html
#
################################################################

print('Please email feedback to esg-support@earthsystemgrid.org.\n')

data = [
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/WSPDSRFAV/b.e21.BHISTcmip6.f09_g17.LE2-1231.001.cam.h0.WSPDSRFAV.199001-199912.nc','filename':'b.e21.BHISTcmip6.f09_g17.LE2-1231.001.cam.h0.WSPDSRFAV.199001-199912.nc','bytes':'19468928','md5Checksum':'1f6fc0ea04ff225747bfa0e1d1a3da36'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/WSPDSRFAV/b.e21.BHISTcmip6.f09_g17.LE2-1231.002.cam.h0.WSPDSRFAV.198001-198912.nc','filename':'b.e21.BHISTcmip6.f09_g17.LE2-1231.002.cam.h0.WSPDSRFAV.198001-198912.nc','bytes':'19472382','md5Checksum':'d950add9917b23a17f979b4e3be3f739'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/WSPDSRFAV/b.e21.BHISTcmip6.f09_g17.LE2-1231.002.cam.h0.WSPDSRFAV.199001-199912.nc','filename':'b.e21.BHISTcmip6.f09_g17.LE2-1231.002.cam.h0.WSPDSRFAV.199001-199912.nc','bytes':'19468740','md5Checksum':'31e319b2ee4791b5529f99bc6eaba614'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/WSPDSRFAV/b.e21.BHISTcmip6.f09_g17.LE2-1231.002.cam.h0.WSPDSRFAV.200001-200912.nc','filename':'b.e21.BHISTcmip6.f09_g17.LE2-1231.002.cam.h0.WSPDSRFAV.200001-200912.nc','bytes':'19469709','md5Checksum':'2bf473e45aff571064a918e9dc0008aa'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/WSPDSRFAV/b.e21.BHISTcmip6.f09_g17.LE2-1231.003.cam.h0.WSPDSRFAV.199001-199912.nc','filename':'b.e21.BHISTcmip6.f09_g17.LE2-1231.003.cam.h0.WSPDSRFAV.199001-199912.nc','bytes':'19463798','md5Checksum':'3bb88c50f8b2a1c7ec74c39e58c61c52'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/WSPDSRFAV/b.e21.BHISTcmip6.f09_g17.LE2-1231.004.cam.h0.WSPDSRFAV.197001-197912.nc','filename':'b.e21.BHISTcmip6.f09_g17.LE2-1231.004.cam.h0.WSPDSRFAV.197001-197912.nc','bytes':'19628842','md5Checksum':'33542893fad08608e073984aae973fe2'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/WSPDSRFAV/b.e21.BHISTcmip6.f09_g17.LE2-1231.004.cam.h0.WSPDSRFAV.200001-200912.nc','filename':'b.e21.BHISTcmip6.f09_g17.LE2-1231.004.cam.h0.WSPDSRFAV.200001-200912.nc','bytes':'19616772','md5Checksum':'669fd3984a830b3a2b9ce44eba626a22'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/WSPDSRFAV/b.e21.BHISTcmip6.f09_g17.LE2-1231.005.cam.h0.WSPDSRFAV.197001-197912.nc','filename':'b.e21.BHISTcmip6.f09_g17.LE2-1231.005.cam.h0.WSPDSRFAV.197001-197912.nc','bytes':'19478042','md5Checksum':'3bae29e760f6d17856e524e57f8aa0d8'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/WSPDSRFAV/b.e21.BHISTcmip6.f09_g17.LE2-1231.008.cam.h0.WSPDSRFAV.198001-198912.nc','filename':'b.e21.BHISTcmip6.f09_g17.LE2-1231.008.cam.h0.WSPDSRFAV.198001-198912.nc','bytes':'19480172','md5Checksum':'74f5ee78dcc7dee598d9d83b67ee87a3'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/WSPDSRFAV/b.e21.BHISTcmip6.f09_g17.LE2-1231.009.cam.h0.WSPDSRFAV.197001-197912.nc','filename':'b.e21.BHISTcmip6.f09_g17.LE2-1231.009.cam.h0.WSPDSRFAV.197001-197912.nc','bytes':'19471701','md5Checksum':'65199c8d0c91ad4ca2c9684174641727'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/WSPDSRFAV/b.e21.BHISTcmip6.f09_g17.LE2-1231.010.cam.h0.WSPDSRFAV.197001-197912.nc','filename':'b.e21.BHISTcmip6.f09_g17.LE2-1231.010.cam.h0.WSPDSRFAV.197001-197912.nc','bytes':'19478642','md5Checksum':'6fe08283c10d9a8261984bf429c8b343'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/WSPDSRFAV/b.e21.BSSP370cmip6.f09_g17.LE2-1231.005.cam.h0.WSPDSRFAV.202501-203412.nc','filename':'b.e21.BSSP370cmip6.f09_g17.LE2-1231.005.cam.h0.WSPDSRFAV.202501-203412.nc','bytes':'19459640','md5Checksum':'ca1f4d2e81df706cd28b4cdf3d88021a'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/WSPDSRFAV/b.e21.BSSP370cmip6.f09_g17.LE2-1231.006.cam.h0.WSPDSRFAV.205501-206412.nc','filename':'b.e21.BSSP370cmip6.f09_g17.LE2-1231.006.cam.h0.WSPDSRFAV.205501-206412.nc','bytes':'19599343','md5Checksum':'7993edd77dff4c4ba0c8c34de5b416df'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/WSPDSRFAV/b.e21.BSSP370cmip6.f09_g17.LE2-1231.007.cam.h0.WSPDSRFAV.205501-206412.nc','filename':'b.e21.BSSP370cmip6.f09_g17.LE2-1231.007.cam.h0.WSPDSRFAV.205501-206412.nc','bytes':'19460977','md5Checksum':'68651e98a08e787df663efeff98580f7'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/WSPDSRFAV/b.e21.BSSP370cmip6.f09_g17.LE2-1231.008.cam.h0.WSPDSRFAV.204501-205412.nc','filename':'b.e21.BSSP370cmip6.f09_g17.LE2-1231.008.cam.h0.WSPDSRFAV.204501-205412.nc','bytes':'19459997','md5Checksum':'a69517aa9ddb169807b77bdd4427f335'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/WSPDSRFAV/b.e21.BSSP370cmip6.f09_g17.LE2-1231.010.cam.h0.WSPDSRFAV.203501-204412.nc','filename':'b.e21.BSSP370cmip6.f09_g17.LE2-1231.010.cam.h0.WSPDSRFAV.203501-204412.nc','bytes':'19609096','md5Checksum':'893bf7302a2107bd977db99506b4e44f'},]

def main(data):

    args = processArguments()

    for d in data:
        executeDownload(Download(args, d))

def processArguments():

    args = {}
    args.update({'apiToken': '6gVAiOJqI4I3oNMuiEstMigjNakfq62LZRHVcwJ0'})
    args.update({'userAgent': 'python/{}/gateway/{}'.format(python_version(), '4.4.4-20240220-190232')})
    args.update({'attemptMax': 10})
    args.update({'initialSleepSeconds': 10})
    args.update({'sleepMultiplier': 3})
    args.update({'sleepMaxSeconds': 900})
    args.update({'insecure': False})

    if '-k' in sys.argv or '--insecure' in sys.argv:
        args.update({'insecure': True})

    if '-h' in sys.argv or '--help' in sys.argv:
        print('Usage: {} [options...]'.format(sys.argv[0]))
        print(' -h, --help        Show usage')
        print(' -k, --insecure    Allow insecure server connections (no certificate check) when using SSL')
        exit(0)

    return args

def executeDownload(download):

    if not os.path.isfile(download.filename):
        attemptAndValidateDownload(download)
        moveDownload(download)
    else:
        download.success = True
        download.valid = True

    reportDownload(download)

def moveDownload(download):

    if download.success and (download.valid or download.vwarning):
        os.rename(download.filenamePart, download.filename)

def reportDownload(download):

    if download.success and download.valid:
        print('{} download successful'.format(download.filename))

    if download.success and not download.valid and download.vwarning:
        print('{} download validation warning: {}'.format(download.filename, download.vwarning))

    if download.success and not download.valid and download.verror:
        print('{} download validation error: {}'.format(download.filename, download.verror))

    if not download.success and download.error:
        print('{} download failed: {}'.format(download.filename, download.error))

def attemptAndValidateDownload(download):

    while download.attempt:
        downloadFile(download)

    if download.success:
        validateFile(download)

def downloadFile(download):

    try :
        startOrResumeDownload(download)
    except HTTPError as error:
        handleHTTPErrorAttempt(download, error)
    except URLError as error:
        handleRecoverableAttempt(download, error)
    except TimeoutError as error:
        handleRecoverableAttempt(download, error)
    except Exception as error:
        handleIrrecoverableAttempt(download, error)
    else:
        handleSuccessfulAttempt(download)

def startOrResumeDownload(download):

    startAnimateDownload('{} downloading:'.format(download.filename))

    if os.path.isfile(download.filenamePart):
        resumeDownloadFile(download)
    else:
        startDownloadFile(download)

def startAnimateDownload(message):
    global animateMessage
    global animateOn

    animateMessage = message
    animateOn = True

    # making the animation run as a daemon thread allows it to
    # exit when the parent (main) is terminated or killed
    t = threading.Thread(daemon=True, target=animateDownload)
    t.start()

def stopAnimateDownload(outcome):
    global animateOutcome
    global animateOn

    animateOutcome = outcome
    animateOn = False

    # wait for animation child process to stop before any parent print
    time.sleep(0.3)

def animateDownload():
    global animateMessage
    global animateOutcome
    global animateOn

    for d in itertools.cycle(['.  ', '.. ', '...', '   ']):

        if not animateOn:
            print('\r{} {}'.format(animateMessage, animateOutcome), flush=True)
            break

        print('\r{} {}'.format(animateMessage, d), end='', flush=True)
        time.sleep(0.2)

def resumeDownloadFile(download):

    request = createRequest(download, createResumeHeaders(download))
    readFile(download, request)

def startDownloadFile(download):

    request = createRequest(download, createStartHeaders(download))
    readFile(download, request)

def createResumeHeaders(download):

    headers = createStartHeaders(download)
    headers.update(createRangeHeader(download))

    return headers

def createRequest(download, headers):

    request = urllib.request.Request(download.url, headers=headers)

    return request

def createStartHeaders(download):

    headers = {}
    headers.update(createUserAgentHeader(download))

    if download.apiToken:
        headers.update(createAuthorizationHeader(download))

    return headers

def createUserAgentHeader(download):

    return {'User-agent': download.userAgent}

def createAuthorizationHeader(download):

    return {'Authorization': 'api-token {}'.format(download.apiToken)}

def createRangeHeader(download):

    start = os.path.getsize(download.filenamePart)
    header = {'Range': 'bytes={}-'.format(start)}

    return header

def readFile(download, request):

    context = createSSLContext(download)

    with urllib.request.urlopen(request, context=context) as response, open(download.filenamePart, 'ab') as fh:
        collectResponseHeaders(download, response)
        shutil.copyfileobj(response, fh)

def createSSLContext(download):

    # See:
    #      https://docs.python.org/3/library/urllib.request.html
    #      https://docs.python.org/3/library/http.client.html#http.client.HTTPSConnection
    #      https://docs.python.org/3/library/ssl.html#ssl.SSLContext
    #
    # Excerpts:
    #      If context is specified it must be a ssl.SSLContext instance...
    #      http.client.HTTPSConnection performs all the necessary certificate and hostname checks by default.

    if download.insecure:
        return ssl._create_unverified_context()

    return None

def collectResponseHeaders(download, response):

    download.responseHeaders = response.info()
    if download.responseHeaders.get('ETag'):
        download.etag = download.responseHeaders.get('ETag').strip('"')

def handleHTTPErrorAttempt(download, httpError):

    if httpError.code == 416: # 416 is Range Not Satisfiable
        # likely the file completely downloaded and validation was interrupted,
        # therefore calling it successfully downloaded and allowing validation
        # to say otherwise
        handleSuccessfulAttempt(download)
    else:
        handleRecoverableAttempt(download, httpError)

def handleRecoverableAttempt(download, error):

    stopAnimateDownload('error')

    print('failure on attempt {} downloading {}: {}'.format(download.attemptNumber, download.filename, error))

    if download.attemptNumber < download.attemptMax:
        sleepBeforeNextAttempt(download)
        download.attemptNumber += 1
    else:
        download.attempt = False
        download.error = error

def sleepBeforeNextAttempt(download):

    sleepSeconds = download.initialSleepSeconds * (download.sleepMultiplier ** (download.attemptNumber - 1))

    if sleepSeconds > download.sleepMaxSeconds:
        sleepSeconds = download.sleepMaxSeconds

    print('waiting {} seconds before next attempt to download {}'.format(sleepSeconds, download.filename))
    time.sleep(sleepSeconds)

def handleIrrecoverableAttempt(download, error):

    stopAnimateDownload('error')

    download.attempt = False
    download.error = error

def handleSuccessfulAttempt(download):

    stopAnimateDownload('done')

    download.attempt = False
    download.success = True

def validateFile(download):

    try:
        validateAllSteps(download)
    except InvalidDownload as error:
        download.valid = False
        download.vwarning = str(error)
    except Exception as error:
        download.valid = False
        download.verror = error
    else:
        download.valid = True

def validateAllSteps(download):

    verrorData = validatePerData(download)
    verrorEtag = validatePerEtag(download)
    verrorStale = validateStaleness(download)

    if verrorData and verrorEtag:
        raise verrorData

    if verrorStale:
        raise verrorStale

def validatePerData(download):

    try:
        validateBytes(download)
        validateChecksum(download)
    except InvalidDownload as error:
        return error
    else:
        return None

def validateBytes(download):

    size = os.path.getsize(download.filenamePart)
    if not download.bytes == size:
        raise InvalidSizeValue(download, size)

def validateChecksum(download):

    if download.md5Checksum:
        md5Checksum = readMd5Checksum(download)
        if not download.md5Checksum == md5Checksum:
            raise InvalidChecksumValue(download, md5Checksum)
    else:
        raise UnableToPerformChecksum(download)

def readMd5Checksum(download):

    hash_md5 = hashlib.md5()

    with open(download.filenamePart, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_md5.update(chunk)

    return hash_md5.hexdigest()

def validatePerEtag(download):

    try:
        validateChecksumEtag(download)
    except InvalidDownload as error:
        return error
    else:
        return None

def validateChecksumEtag(download):

    if isEtagChecksum(download):
        md5Checksum = readMd5Checksum(download)
        if not download.etag == md5Checksum:
            raise InvalidChecksumValuePerEtag(download, md5Checksum)
    else:
        raise UnableToPerformChecksum(download)

def isEtagChecksum(download):

    return download.etag and re.fullmatch(r'[a-z0-9]+', download.etag)

def validateStaleness(download):

    try:
        validateStaleChecksum(download)
    except InvalidDownload as error:
        return error
    else:
        return None

def validateStaleChecksum(download):

    if isEtagChecksum(download):
        if not download.md5Checksum or download.md5Checksum != download.etag:
            raise StaleChecksumValue(download)

class InvalidDownload(Exception):

    pass

class InvalidSizeValue(InvalidDownload):

    def __init__(self, download, actual):
        super().__init__('invalid byte size for {}: downloaded file is {} bytes but should be {}'.format(download.filename, actual, download.bytes))

class InvalidChecksumValue(InvalidDownload):

    def __init__(self, download, actual):
        super().__init__('invalid checksum for {}: downloaded file is {} but should be {}'.format(download.filename, actual, download.md5Checksum))

class InvalidChecksumValuePerEtag(InvalidDownload):

    def __init__(self, download, actual):
        super().__init__('invalid checksum for {}: downloaded file is {} but should be {} according to server'.format(download.filename, actual, download.etag))

class UnableToPerformChecksum(InvalidDownload):

    def __init__(self, download):
        super().__init__('cannot verify checksum of {}'.format(download.filename))

class StaleChecksumValue(InvalidDownload):

    def __init__(self, download):
        super().__init__('checksum value has changed for {}'.format(download.filename))

class Download():

    def __init__(self, args, datum):

        self.apiToken = args.get('apiToken')
        self.userAgent = args.get('userAgent')
        self.attemptMax = args.get('attemptMax')
        self.initialSleepSeconds = args.get('initialSleepSeconds')
        self.sleepMultiplier = args.get('sleepMultiplier')
        self.sleepMaxSeconds = args.get('sleepMaxSeconds')
        self.insecure = args.get('insecure')

        self.url = datum.get('url')
        self.filename = datum.get('filename')
        self.bytes = int(datum.get('bytes'))
        self.md5Checksum = datum.get('md5Checksum')

        self.filenamePart = self.filename + '.part'
        self.success = False
        self.attempt = True
        self.attemptNumber = 1
        self.responseHeaders = {}
        self.etag = None
        self.error = None
        self.valid = False
        self.vwarning = None
        self.verror = None

    def __str__(self):
        return f'url: {self.url}, filename: {self.filename}, bytes: {self.bytes}, md5Checksum: {self.md5Checksum}'

if __name__ == '__main__':
    main(data)
