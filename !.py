import pymel.core as pm


# clean up previous experiment
pm.newFile(force=True)

#create constraint system
pm.spaceLocator(name="master")
master=pm.PyNode("master")
pm.polyCube(name="slave")
slave=pm.PyNode("slave")
slave.tx.set(10)


constraint = pm.parentConstraint(master,slave,name="constraint", maintainOffset=True)

#create network node
grabit_network=pm.createNode("network",name="grabit_NET")

# add message attributes to network
pm.addAttr(grabit_network, attributeType="message",longName="constraint")
pm.addAttr(grabit_network, attributeType="message",longName="master")
pm.addAttr(grabit_network, attributeType="message",longName="slave")

# connect node.message to network's attrs
# this node.message attr seems to be hidden and always present on nodes
constraint.message >> grabit_network.constraint
master.message >> grabit_network.master
slave.message >> grabit_network.slave

# the reverse does not work, not sure why...
# grabit_network.constraint >> constraint.message
# grabit_network.master >> master.message
# grabit_network.slave >> slave.message

# after reload of the maya file, list the constraint system elements
# the .get() of a message attr returns the actual node, so no need for listConnections()
constraint= grabit_network.constraint.get()
master= grabit_network.master.get()
slave= grabit_network.slave.get()

print constraint, type(constraint)
print master, type(master)
print slave, type(slave)