Introduction
============

This add-on provide scss integration into Plone. It use python implementation
from Kirill Klenov available on github: https://github.com/klen/python-scss

How to use scss with Plone
==========================

You have to create your stylesheet like a browser view. Registering a
mysheet.scss this way::

    <browser:page
      name="mysheet.scss"
      for="*"
      class="collective.scss.stylesheet.SCSSView"
      template="mysheet.pt"
      permission="zope2.View
      />

Create a mysheet.pt file in the same folder, and register your stylesheet in the
portal_css tool. Using a GenericSetup profile you just have to add an entry in 
the cssregistry.xml file and apply the profile::

    <?xml version="1.0"?>
    <object name="portal_css">
     <stylesheet title=""
        id="mysheet.scss"
        media="screen" rel="stylesheet" rendering="import"
        cacheable="True" compression="safe" cookable="True"
        enabled="1" expression="" />
    </object>

