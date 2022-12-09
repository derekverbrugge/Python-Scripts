# ConvertDataToXML.py
# This python script creates an XML file. 
#  -Derek Verbrugge

import xml.etree.ElementTree as ET

# Create the root element
root = ET.Element('root')

# Create a sub-element
data = ET.SubElement(root, 'data')

# Add some text to the sub-element
data.text = 'This is the data that we want to convert to XML'

# Create an XML tree from the Element
tree = ET.ElementTree(root)

# Write the XML tree to a file
with open('data.xml', 'wb') as f:
  tree.write(f)
