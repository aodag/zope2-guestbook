guestbook
==============

これは Zope2 で five.grok を使ったアプリケーションの練習として作成したものです。


INSTALL
================

PyPIにアップロードしたりしないので、 mr.developer を使ってください。
ベースとなるbuildout.cfgは `Zope Developer's Guid <http://docs.zope.org/zope2/zdgbook/GettingStarted.html#installing-zope-2>`_ のものを想定しています。

::

  [sources]
  guestbook = git git@github.com:aodag/zope2-guestbook.git

guestbook.cfg::

  [buildout]
  extends = buildout.cfg

  [instance]
  eggs += guestbook

activate::

  $ bin/develop co guestbook
  $ bin/buildout -c guestbook.cfg

run Zope2::

  $ bin/instance fg
