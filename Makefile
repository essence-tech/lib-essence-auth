default: interface

.phony: interface
interface:
	protoc \
		-I. \
		-I/usr/local/lib \
		-I$$GOPATH/src \
		-I$$GOPATH/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
		--go_out=Mgoogle/api/annotations.proto=github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis/google/api,plugins=grpc:essenceauth \
		auth.proto
	protoc \
		-I. \
		-I/usr/local/lib \
		-I$$GOPATH/src \
		-I$$GOPATH/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
		--grpc-gateway_out=logtostderr=true:essenceauth \
		auth.proto
	python \
		-m grpc.tools.protoc \
		-I. \
		-I/usr/local/lib \
		-I$$GOPATH/src \
		-I$$GOPATH/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
		--python_out=essenceauth/. \
		--grpc_python_out=essenceauth/. \
		auth.proto
