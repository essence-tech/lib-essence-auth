default: codegen

.phony: codegen
codegen:
	protoc -I/usr/local/include -I. \
		-I$$GOPATH/src \
		-I$$GOPATH/src/github.com/googleapis/googleapis/ \
		--go_out=,plugins=grpc:essenceauth \
		auth.proto
	python \
		-m grpc.tools.protoc \
		--python_out=. \
		--grpc_python_out=. \
		-I$$GOPATH/src/github.com/googleapis/googleapis \
		$$GOPATH/src/github.com/googleapis/googleapis/google/api/annotations.proto
	python \
		-m grpc.tools.protoc \
		--python_out=. \
		--grpc_python_out=. \
		-I$$GOPATH/src/github.com/googleapis/googleapis \
		$$GOPATH/src/github.com/googleapis/googleapis/google/api/http.proto
	touch google/api/__init__.py
	python \
		-m grpc.tools.protoc \
		--python_out=essenceauth/. \
		--grpc_python_out=essenceauth/. \
		-I. \
		-I/usr/local/lib \
		-I$$GOPATH/src \
		-I$$GOPATH/src/github.com/googleapis/googleapis \
		auth.proto
	protoc -I/usr/local/include -I. \
		-I$$GOPATH/src \
		-I$$GOPATH/src/github.com/googleapis/googleapis \
		--grpc-gateway_out=logtostderr=true:essenceauth \
		auth.proto
