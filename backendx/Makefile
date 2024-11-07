help:
	@echo make ray-start
	@echo make ray-stop
	@echo make ray-status
	@echo ""
	@echo make open-ray-dashboard
	@echo ""
	@echo make serve-status
	@echo make serve-shutdown	
	@echo ""
	@echo make hello
	@echo make test-hello
	@echo ""
	@echo make run3
	@echo make test3
	@echo make all3
	@echo ""
	@echo make hello-composite
	@echo make test-hello-composite
	@echo ""
	@echo make sky-laumch
	@echo make sky-laumch2
	@echo make sky-laumch3	

# NA
# - replace with with conda create -f conda.yml
# NOTE:
# - M1 mac issue may require manual reset of grpcio
#   conda update -n base -c conda-forge conda
# 	pip uninstall grpcio; conda install grpcio
# env:
#	python3 -m venv venv

# NA
# - replace with with conda create -f conda.yml
# install:
#	python3 -m pip install --upgrade pip
#	pip install -r requirements.txt

ray-start:
	ray start --head

ray-stop:
	ray stop

ray-status:
	ray status

open-ray-dashboard:
	open "http://127.0.0.1:8265"	

serve-status:
	serve status

serve-shutdown:
	serve shutdown -y

# NA
# - deprecated
# run3: serve-shutdown ray-stop ray-start
# 	python3 iris_ml_server.py	
# test3:
# 	python3 test_iris_predict.py
# all3: run2 test2

# NA
# - original experiment
# @echo health check 1
# curl -X GET -H "Origin: http://localhost" http://localhost:8000/api1/
# @echo ""
# @echo health check 2
# curl -X GET -H "Origin: http://localhost" http://localhost:8000/api2/			
# @echo ""
# @echo predict 1
# curl -X GET -H "Origin: http://localhost" http://localhost:8000/api1/predict
# @echo ""
# @echo predict 2
# curl -X GET -H "Origin: http://localhost" http://localhost:8000/api2/predict?x=1
# @echo ""
run: serve-shutdown ray-stop ray-start
	python3 main.py
test:
	@echo predict 3
	curl -X GET http://localhost:8000/api3/predict?x=1	
	@echo ""
all: run test

# NA
# - test sky remote with simple web serve
hello:
	python3 hello.py
test-hello:
	python test_hello.py
open-hello:
	open http://localhost:8000/docs
test-hello-remote:
	. ./test_hello_remote.sh

# NA
# - just get composite working manually
run2: serve-shutdown ray-stop ray-start
	python3 main2.py
test2:
	python3 test_main2.py
all2: run2 test2

# NA
# - refactor to prepare for sky launch and remote testing
run3: serve-shutdown ray-stop ray-start
	python3 main3.py
test3:
	python3 test_main3.py
all2: run3 test3
test3-remote:
	. ./test_main3_remote.sh

hello-pipeline: serve-shutdown ray-stop ray-start
	python3 hello_pipeline.py
test-hello-pipeline:
	python3 test_hello_pipeline.py
# test-hello-pipeline-remote:

# NA
# Q: serve.run vs. serve.start vs. serve build
# serve build hello_pipeline:app -o config.yaml

sky-launch:
	sky launch -c main3 infra/sky-main3.yaml -i 10

sky-launch2:
	sky launch -c my-ray infra/sky-my-ray2_8.yaml -i 10

sky-launch3:
	sky launch -c pipeline infra/sky-hello-pipeline.yaml -i 10
