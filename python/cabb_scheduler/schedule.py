# A schedule is a collection of scans, so the schedule class
# doesn't do much. But we do keep track of certain constants.
from scan import scan

class schedule:
    def __init__(self):
        # This is the list of scans, in order.
        self.scans = []
        return None
        
    def addScan(self, options={}):
        # Add a scan to the schedule.
        scan_new = scan()

        # By default, we copy the details from the previous scan.
        if (not ('nocopy' in options and options['nocopy'] == True)) and (len(self.scans) > 0):
            scan_old = self.scans[-1]
            scan_new.setSource(scan_old.getSource())
            scan_new.setRightAscension(scan_old.getRightAscension())
            scan_new.setDeclination(scan_old.getDeclination())
            scan_new.setEpoch(scan_old.getEpoch())
            scan_new.setCalCode(scan_old.getCalCode())
            scan_new.setScanLength(scan_old.getScanLength())
            scan_new.setScanType(scan_old.getScanType())
        
        # Check for options for the scan.
        if 'source' in options:
            scan_new.setSource(options['source'])
        if 'rightAscension' in options:
            scan_new.setRightAscension(options['rightAscension'])
        if 'declination' in options:
            scan_new.setDeclination(options['declination'])
        if 'epoch' in options:
            scan_new.setEpoch(options['epoch'])
        if 'calCode' in options:
            scan_new.setCalCode(options['calCode'])
        if 'scanLength' in options:
            scan_new.setScanLength(options['scanLength'])
        if 'scanType' in options:
            scan_new.setScanType(options['scanType'])
            
        # Add the scan to the list.
        self.scans.append(scan_new)
            
        return scan_new

    def write(self, name=None):
        # Write out the schedule to disk.
        if name is not None:
            with open(name, 'w') as schedFile:
                for i in xrange(0, len(self.scans)):
                    schedFile.write("$SCAN*V5\n")
                    if (i == 0) or (self.scans[i].getSource() !=
                                    self.scans[i - 1].getSource()):
                        schedFile.write("Source=%s\n" % self.scans[i].getSource())
                    if (i == 0) or (self.scans[i].getRightAscension() !=
                                    self.scans[i - 1].getRightAscension()):
                        schedFile.write("RA=%s\n" % self.scans[i].getRightAscension())
                    schedFile.write("$SCANEND\n")
        return self
