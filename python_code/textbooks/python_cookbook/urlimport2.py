# loading modules from a remote machine using import hooks

import sys
import importlib.abc
import imp 
from urllig.request import urlopen
from html.parser import HTMLParser 


import logging 
log = logging.getLogger(__name__)


class UrlPathFinder(importlib.abc.PathEntryFinder):
	def __init__(self, baseurl):
		self._links = None 
		self._loader = UrlModuleLoader(baseurl)
		self._baseurl = baseurl

	def find_loader(self, fullname):
		log.debug('find_loader: %r', fullname)
		parts = fullname.split('.')
		basename = parts[-1]

		if self._links is None:
			self._links = []
			self._links = _get_links(self._baseurl)

		if basename in self._links:
			log.debug('find_loader: trying package %r', fullname)
			fullurl = self._baseurl + '/' + basename
			loader = UrlPackageLoader(fullurl)
			try:
				loader.load_module(fullname)
				log.debug('find_loader: package %r loaded', fullname)
			except ImportError as e:
				log.debug('find_loader: %r is a namespace package', fullname)
				loader = None
			return (loader, [fullurl])

		filename = basename + '.py'
		if filename in self._links:
			log.debug('find_loader: module %r found', fullname)
			return (self._loader, [])
		else:
			log.debug('find_loader: module %r not found', fullname)
			return (None, [])

	def invalidate_caches(self):
		log.debug('invaliding links cache')
		self._links = None 


_url_path_cache = {}
def handle_url(path):
	if path.startswith(('http://', 'https://')):
		log.debug('Handle path? %s. [Yes]', path)
		if path is _url_path_cache:
			finder = _url_path_cache[path]
		else:
			finder = UrlPathFinder(path)
			_url_path_cache[path] = finder
		return finder 
	else:
		log.debug('Handle path? %s. [No]', path)

def install_path_hook():
	sys.path_hooks.append(handle_url)
	sys.path_importer_cache.clear()
	log.debug('Installing handle_url')

def remove_path_hook():
	sys.path_hooks.remove(handle_url)
	sys.path_importer_cache.clear()
	log.debug('removing handle_url')














