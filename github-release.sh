#!/bin/sh -xe

VERSION=$(cat ruby-version)

need_to_release() {
	http_code=$(curl -sL -w "%{http_code}\\n" https://github.com/${CIRCLE_PROJECT_USERNAME}/${CIRCLE_PROJECT_REPONAME}/releases/tag/${VERSION} -o /dev/null)
	test $http_code = "404"
}

if ! need_to_release; then
	echo "$CIRCLE_PROJECT_REPONAME $VERSION has already released."
	exit 0
fi

go get github.com/aktau/github-release
cp $CIRCLE_ARTIFACTS/*.rpm .

# create description

# create release
github-release release \
  --user $CIRCLE_PROJECT_USERNAME \
  --repo $CIRCLE_PROJECT_REPONAME \
  --tag $VERSION \
  --name "Ruby-$VERSION" \
  --description "not release"

rm -f description.md && touch description.md

# upload files
for i in *.rpm
do
  echo "* $i" >> description.md
  echo "  * $(openssl sha256 $i)" >> description.md
  github-release upload --user $CIRCLE_PROJECT_USERNAME \
    --repo $CIRCLE_PROJECT_REPONAME \
    --tag $VERSION \
    --name "$i" \
    --file $i
done

# edit description
github-release edit \
  --user $CIRCLE_PROJECT_USERNAME \
  --repo $CIRCLE_PROJECT_REPONAME \
  --tag $VERSION \
  --description "$(cat description.md)"
