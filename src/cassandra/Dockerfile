FROM cassandra
RUN sed -i 's/^start_rpc.*$/start_rpc: true/' /etc/cassandra/cassandra.yaml
RUN sed -i 's/^rpc_address.*$/rpc_address: cassandra/' /etc/cassandra/cassandra.yaml
