FROM databricksruntime/python:latest

# Install OpenJDK 17 and other system dependencies
USER root
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    openjdk-17-jdk \
    procps \
    wget \
    tar \
    python3-pip \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

# Install Apache Spark 3.5.2
ENV SPARK_VERSION=3.5.2
ENV HADOOP_VERSION=3
ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/bin:$PATH
ENV PYTHONPATH=/app

RUN wget -q "https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" && \
    tar xzf spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz -C /opt/ && \
    mv /opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} $SPARK_HOME && \
    rm spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz

# Download dependencies JARs for Delta Lake and AWS (MinIO)
# versions must match Spark 3.5.x
RUN cd $SPARK_HOME/jars && \
    wget -q https://repo1.maven.org/maven2/io/delta/delta-spark_2.12/3.2.0/delta-spark_2.12-3.2.0.jar && \
    wget -q https://repo1.maven.org/maven2/io/delta/delta-storage/3.2.0/delta-storage-3.2.0.jar && \
    wget -q https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar && \
    wget -q https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar && \
    wget -q https://repo1.maven.org/maven2/org/postgresql/postgresql/42.6.0/postgresql-42.6.0.jar

# Set working directory
WORKDIR /app

COPY . .

CMD ["/bin/bash"]
