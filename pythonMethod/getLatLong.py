import exifread

def degToDec(coord):

    latdec = float(coord[0][0].num)/coord[0][0].den+float(coord[0][1].num)/coord[0][1].den/60 + float(coord[0][2].num)/coord[0][2].den/3600
    if coord[2] == 'S':
        latdec = latdec*-1

    lngdec = float(coord[1][0].num)/coord[1][0].den+float(coord[1][1].num)/coord[1][1].den/60 + float(coord[1][2].num)/coord[1][2].den/3600
    if coord[3] == 'W':
        lngdec = lngdec*-1

    return (latdec,lngdec)
    
def getLatLong(fileLoc):
#pass in file location as fileLoc (string). don't forget .jpg!
#returns lat and long as list = (lat,long)

    f = open(fileLoc,'rb')
    metadata = exifread.process_file(f,details=False)

    for key in metadata.keys():
        if key ==  'GPS GPSLatitude':
            lat = metadata[key]
        elif key == 'GPS GPSLongitude':
            lng = metadata[key]
        elif key == 'GPS GPSLatitudeRef':
            latdir = str(metadata[key])
        elif key == 'GPS GPSLongitudeRef':
            lngdir = str(metadata[key])
    
    lats = lat.values
    lngs = lng.values
    
    return degToDec([lats,lngs,latdir,lngdir])

#print(getLatLong('100075_lowres.jpg'))
