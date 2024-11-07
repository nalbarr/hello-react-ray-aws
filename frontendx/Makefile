help:
	@echo make install
	@echo ""
	@echo make format-check
	@echo make format
	@echo make lint
	@echo ""
	@echo make set-base-url
	@echo make dump-base-url
	@echo ""
	@echo make run
	@echo make test
	@echo ""
	@echo make clean

init:
	npm init @eslint/config
	npm install -g yarn
	yarn add --dev --exact prettier

install:
	yarn install

format-check:
	yarn prettier --check "src/**/*.js"

format:
	yarn prettier --write "src/**/*.js"

lint:
	yarn eslint

set-base-url:
	# NA.
	# NOTE: MP you need to source set_base_url.sh to export HTTPCLIENT_BASE_URL
	cp .env.bak .env
	sed -i -e 's/XXX/$(TARGET_IP_ADDRESS)/g' .env
	node dumpBaseUrl.js

run: set-base-url
	# NA. 
	# NOTE: MP - you will need below to expose nodejs and vite.js outside of localhost
	# yarn dev
	yarn dev --host

dump-base-url:
	node dumpBaseUrl.js

# curl -X GET -H "Origin: http://localhost" http://localhost:8000/api3/predict?x=1
test:
	@echo predict 3
	curl -X GET $(HTTPCLIENT_BASE_URL)/api3/predict?x=1
	@echo ""

clean:
	rm -rf ./node_modules
