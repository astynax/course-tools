FROM python:3.6-alpine

RUN apk add --no-cache make

WORKDIR /build

ADD . .

# install pandoc
RUN make -f docker.make pandoc

# install poetry
RUN pip install -U poetry

# install tools
RUN make -f docker.make tools

WORKDIR /work

CMD echo "usage reorg|scaffold|pandoc"
