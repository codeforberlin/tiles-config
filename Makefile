api:
	uvicorn gdal_tiles_api.main:app \
	    --reload  \
		--reload-dir ~/code/codeforberlin/gdal-tiles-api \
		--reload-dir . \
		--reload-include '*.toml'

titiler:
	uvicorn titiler.application.main:app --port=5000
