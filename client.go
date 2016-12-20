package essenceauth

import (
	"log"

	"github.com/essence-tech/lib-essence-auth/essenceauth"
	"google.golang.org/grpc"
)

// Service provides access to auth.
type Service interface {
	essenceauth.EssenceAuthClient
	Close()
}

type serviceClient struct {
	essenceauth.EssenceAuthClient
	conn *grpc.ClientConn
}

// New returns a new Service instance with default options.
func New(host string) Service {
	conn, err := grpc.Dial(host, grpc.WithInsecure())
	if err != nil {
		log.Fatal(err)
	}

	_client := essenceauth.NewEssenceAuthClient(conn)
	return &serviceClient{_client, conn}
}

// Close closes the connection to the service.
func (s *serviceClient) Close() {
	s.conn.Close()
}
