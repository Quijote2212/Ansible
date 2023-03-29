import java.lang.Runtime as Runtime

clusters = AdminConfig.list("ServerCluster").splitlines()

for cluster in clusters:
    cluster_name = AdminConfig.showAttribute(cluster, "name")
    print("Starting cluster: " + cluster_name)
    servers = AdminConfig.list("ClusterMember", cluster).splitlines()
    for server in servers:
        server_name = AdminConfig.showAttribute(server, "memberName")
        node_name = AdminConfig.showAttribute(server, "nodeName")
        print("Starting server: " + server_name + " on node: " + node_name)
        process = Runtime.getRuntime().exec("wsadmin.sh -lang jython -c 'AdminControl.startServer(\"" + server_name + "\", \"" + node_name + "\", \"-cluster\", \"" + cluster_name + "\")'")
        process.waitFor()
    print("Cluster started: " + cluster_name)
