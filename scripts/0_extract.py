import zipfile
import re
import io

root = "submissions.zip"
prefix = 'cameraready'

# Open root file
with zipfile.ZipFile(root) as ziproot:
    print('# Opening root:', ziproot)

    # Iterate members
    for rootmember in ziproot.namelist():
        # Split name and extension
        filename, extension = rootmember.split('.')

        # Get AID number from filename
        aid = int(re.sub('\D', '', filename))

        # Analyze only members starting with prefix
        if filename.startswith(prefix):
            
            # Validate extensions
            if extension == 'zip':

                # If zip ~ extract it to bytesIO
                with ziproot.open(rootmember) as binaryfile:
                    with zipfile.ZipFile(io.BytesIO(binaryfile.read())) as zipmember:
                        
                        zips_in_member = [x for x in zipmember.namelist() 
                                          if x.endswith('.zip')]
                        
                        if len(zips_in_member) > 0:
                            print('%', 'SOURCES FOR ARTICLE', aid, 'in file', zips_in_member[0])

                            with zipmember.open(zips_in_member[0]) as lastbinaryfile:
                                with zipfile.ZipFile(io.BytesIO(lastbinaryfile.read())) as lastzip:
                                    lastzip.extractall('submissions/%04i/' % aid)
                                    



                        else:
                            print('! NO SOURCES FOR ARTICLE', aid, '- zip without zip')
                        
            elif extension == 'pdf':
                print('! NO SOURCES FOR ARTICLE', aid, '- only pdf')

    exit()
        