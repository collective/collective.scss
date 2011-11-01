Introduction
============

This add-on provide scss_ integration into Plone. It use python implementation
from Kirill Klenov available on github_.

You will be able to write scss stylesheets and register them into the css
registry (portal_css).

How to use scss with Plone
==========================

You have to create a new file (mysheet.scss). Next register a css stylesheet
as a browser view using your scss file::

    <browser:page
      name="mysheet.css"
      for="*"
      class="collective.scss.stylesheet.SCSSView"
      template="mysheet.scss"
      permission="zope2.View
      />

Now you just have to register your stylesheet in the css registry. 
Using a GenericSetup profile you just have to add an entry in 
the cssregistry.xml file, restart your zope server and apply the profile::

    <?xml version="1.0"?>
    <object name="portal_css">
     <stylesheet title=""
        id="mysheet.css"
        media="screen" rel="stylesheet" rendering="import"
        cacheable="True" compression="safe" cookable="True"
        enabled="1" expression="" />
    </object>


Credits
=======

Companies
---------

|makinacom|_

  * `Planet Makina Corpus <http://www.makina-corpus.org>`_
  * `Contact us <mailto:python@makina-corpus.org>`_


Authors

  - JeanMichel FRANCOIS aka toutpt <toutpt@gmail.com>


.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com
.. _scss: http://sass-lang.com/
.. _github: https://github.com/klen/python-scss
