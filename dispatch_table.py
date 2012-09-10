
#import os


dispath_table = {

	"/index" : (web.index,
		webpublisher.GET
		)
	
	"/param" :(web.param,
		webpublisher.GET
		)

	"/getbagr" : (web.bagr,
		webplisher.GET
		)
}
