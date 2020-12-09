#!/bin/python

from osmapi import OsmApi

MyApi = OsmApi(username = u"coulona28@gmail.com", password = u"Croquedinde94")
MyApi.ChangesetCreate({u"comment": u"My first test"})
print(MyApi.NodeCreate({u"lon":1, u"lat":1, u"tag": {}}))
MyApi.ChangesetClose()
