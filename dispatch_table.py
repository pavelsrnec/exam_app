
#import os


dispath_table = {

	"/index" : (web.index,
		webpublisher.GET
		)
	
	"/param" :(web.param,
		webpublisher.GET
		)
}
