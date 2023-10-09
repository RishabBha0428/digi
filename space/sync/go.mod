module digi.dev/digi/space/sync

go 1.15

require (
	digi.dev/digi v0.0.0
	github.com/operator-framework/operator-sdk v0.18.0
	github.com/spf13/pflag v1.0.5
	k8s.io/apimachinery v0.22.3
	sigs.k8s.io/controller-runtime v0.6.3
)

replace (
	digi.dev/digi v0.0.0 => ../../
	digi.dev/digi/space/sync v0.0.0 => ../sync
	github.com/Azure/go-autorest => github.com/Azure/go-autorest v13.3.2+incompatible // Required by OLM
	k8s.io/client-go => k8s.io/client-go v0.18.2 // Required by prometheus-operator
)
