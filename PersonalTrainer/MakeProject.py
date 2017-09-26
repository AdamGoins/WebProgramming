#!/usr/bin/python
from subprocess import check_output
import sys

class MakeProject:
  
  indent = 0
  
  BIN_PATH = "/home/syndicate/.bin/python/"
  SRC_PATH = "/home/syndicate/.bin/src/"
  
  
  def __init__(self):
    self.WORKING_DIRECTORY = self.getPath() + "/"
    self.runScript()

  def runScript(self):
    args = sys.argv[1::]
    self.destination = args[1]
    
    if len(args) < 2:
      print("Error: Missing position arguments. \n  Required: 2" + ",  Given: " + str(len(sys.argv) - 1))
      return
    
    
    rootPath = ""
    
    for target in args:
      self.echo("Creating Directory Structure [" + target + "]...")
      self.createDirectoryStructure(target)
        
  def createDirectoryStructure(self, target):
    # Create root directory
    
    rootPath = self.getPath()
    print("ROOT PATH: " + rootPath)
  
    # Create subdirectories
    subDirectories= {
        "assets"     : False,
        "directives" : False,
        "less"       : False,
        "services"   : False,
        "thirdParty" : False,
        "views"      : False
      }
    
    root = {
        target: subDirectories
      }
    
    root = self.pathifyDict(root, rootPath)
    self.createSubDirectories(root)
    
    
  def createSubDirectories(self, paths):
    self.indent += 1
    
    for key in paths:
      print("Key: " + key)
      print("Value: " + str(paths[key]))
    
    for target in paths.keys():
      if self.isDirectory(target):
        value = paths[target]
        self.echo("Creating Directory [" + target + "]...")
        print("DIR: " + target)
        self.execute("mkdir " + target)
        if value:
          self.createSubDirectories(value)
      else:
        print("Creating File [" + target + "]")
        self.execute("touch " + target)
    self.indent -= 1


    #def createSubDirectories(self, paths):
      #self.indent += 1
    
      #for target in paths.keys():
        
        #if isDirectory(target):
          #value = paths[target]
          #self.echo("Creating Directory: [" + target + "]...")
          #self.execute("mkdir " + target)
          #if value:
            #self.createSubDirectories(value)
        #else:
          #self.echo("Creating File: [" + target + "]")
          #self.execute("touch " + target)
      #self.indent -= 1

  def pathifyDict(self, dictionary, keyPath):
    try:
      for key in dictionary.keys():
        keyPath = keyPath + key
        print("KEYPATH: " + keyPath)
        dictionary[keyPath] = dictionary[key]
        
        del dictionary[key]
        
        value = dictionary[keyPath]
        if value:
          newPath = keyPath + "/"
          print("New Path: " + newPath)
          self.pathifyDict(value, newPath)
        
      return dictionary
    except Exception as e:
      print(e)
    
    
    
    
  def isDirectory(self, filename):
    return "." not in self.getFileName(filename)


  def echo(self, value):
    print(self.getIndent() + value)
    
  def getIndent(self):
    return "  " * self.indent
    

  def execute(self, command):
    result = check_output(command, shell=True)
    return result

  def getFilePath(self, target):
    target = target.replace(self.WORKING_DIRECTORY, "", 1)
    
    target = self.WORKING_DIRECTORY + target
    
    if self.isDirectory(target):
      target += "/"
    return target

  def getFileName(self, filename):
    name = filename[filename.rindex("/") + 1:] if "/" in filename else filename
    return name

  def getPath(self):
    path = str(self.execute("sudo pwd")).replace("\\n", "")

    startIndex = path.index("'") + 1
    endIndex = path.rindex("'")

    return path[startIndex : endIndex] + "/"


project = MakeProject()
