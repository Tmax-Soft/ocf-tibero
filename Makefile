VERSION=1.1
RELEASE=1

SOURCES=$(HOME)/rpmbuild/SOURCES

all: rpm

targz:
	tar --xform "s@^@ocf-tibero-${VERSION}/@" -czf ${SOURCES}/ocf-tibero-${VERSION}.tar.gz tibero

rpm: targz
	rpmbuild --quiet -D "release ${RELEASE}" -D "version ${VERSION}" -bb ocf-tibero.spec
