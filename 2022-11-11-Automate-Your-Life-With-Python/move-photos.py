import os
import shutil
import re
import platform
import datetime

# This script is used to move files from the camera uploads folder in Dropbox to a structured
# photos folder based on year and month the photo was taken.

# Just update the source and target below:
# ================= PARAMETERS ==================
source = "/Users/alex/Dropbox/Camera Uploads"
target = "/Users/alex/Dropbox/Photos"
# ===============================================

# ================= CONSTANTS ===================
DATE_PATTERN = '.*(20\d\d)-?([01]\d)-?([0123]\d).*'
EXTS = ("jpg", "png", "jpeg", "mov", "mp4")
FOLDER_SEP = "/"
# ===============================================

# ================= METHODS =====================
# Get month folder
def getFolder(year, monthNumber):
  if (monthNumber == "01"):
    monthFolder = "01 January"
  elif (monthNumber == "02"):
    monthFolder = "02 February"
  elif (monthNumber == "03"):
    monthFolder = "03 March"
  elif (monthNumber == "04"):
    monthFolder = "04 April"
  elif (monthNumber == "05"):
    monthFolder = "05 May"
  elif (monthNumber == "06"):
    monthFolder = "06 June"
  elif (monthNumber == "07"):
    monthFolder = "07 July"
  elif (monthNumber == "08"):
    monthFolder = "08 August"
  elif (monthNumber == "09"):
    monthFolder = "09 September"
  elif (monthNumber == "10"):
    monthFolder = "10 October"
  elif (monthNumber == "11"):
    monthFolder = "11 November"
  elif (monthNumber == "12"):
    monthFolder = "12 December"
  
  return year + "/" + monthFolder

def get_file_date(folder, filename):
    # If the filename contains a date in the format yyyy-mm-dd or yyyymmdd
    # Then use that to determine date
    matchObj = re.match(DATE_PATTERN, file)
    if (matchObj):
      year = matchObj.group(1)
      month = matchObj.group(2)
      print("Matched on filename date pattern")
    else:
      dateTaken = creation_date(folder + FOLDER_SEP + filename)
      matchObj = re.match(DATE_PATTERN, dateTaken)
      if (matchObj):
        year = matchObj.group(1)
        month = matchObj.group(2)
      else:
        year = "0"
        month = "0"
        print("Failed to get date for photo: " + filename)

    return {"year": year, "month": month}

def creation_date(path_to_file):
    # Try to get the date that a file was created, falling back to when it was
    # last modified if that isn't possible.
    if platform.system() == 'Windows':
        timestamp = os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            timestamp = stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            timestamp = stat.st_mtime
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
# ===============================================

# ================== SCRIPT =====================
# Loop through all the photos in the folder
files = os.listdir(source)
for file in files:
    # Ignore if filename is not a photo or video
    if (file.lower().endswith(tuple(EXTS))):
      # If the filename contains a date in the format yyyy-mm-dd or yyyymmdd
      # Then use that to determine date
      fileData = get_file_date(source, file)
      year = fileData["year"]
      month = fileData["month"]

      if (year == "0" or month == "0"):
        print("Unable to extract date: " + file)
        continue

      # Get folder name from dates
      folder = getFolder(year, month)

      # Create target folder
      targetFolder = target + FOLDER_SEP + folder
      if (not os.path.exists(targetFolder)):
        print("Creating folder: " + targetFolder)
        os.makedirs(targetFolder)

      # Move photo if it doesn't exist
      sourceFile = source + FOLDER_SEP + file
      targetFile = targetFolder + FOLDER_SEP + file
      if (not os.path.exists(targetFile)):
        print("Moving file: " + file)
        shutil.move(sourceFile, targetFile)
      else:
        # If it already exists and is exactly the same size then delete it.
        if os.stat(sourceFile).st_size == os.stat(targetFile).st_size:
          print("Duplicate file, deleting: " + file)
          os.remove(sourceFile)
        else:
          # Might want to rename and move here
          print("Duplicate file, different size: " + file)
# ===============================================