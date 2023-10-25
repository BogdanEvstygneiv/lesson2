FROM centos
RUN yum update
RUN yum install curl wget busybox-extras netcat-openbsd python py-pip bash && \
    pip install awscli

CMD tail -f /dev/null
