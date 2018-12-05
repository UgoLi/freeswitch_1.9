from graphviz import Digraph


def draw_flow(titles,length):
    main_graph = Digraph()
    title_graph = Digraph()
    all_node = {}
    main_graph.graph_attr.update(splines='line')
    for title in titles:
        title_graph.node(title, label=title, color='black', shape ='box')
        node_list = []
        tmp_graph = Digraph()
        for index in range(0, length):
            node_name = str('%s%d' % (title, index))
            node_list.append(node_name)
            if index is 0:
                tmp_graph.edge(title,'%s%d' % (title, index))
            else:
                tmp_graph.edge('%s%d' % (title, index - 1),'%s%d' %(title,index))
        main_graph.subgraph(tmp_graph)
        all_node[title] = node_list

    title_graph.graph_attr.update(rank='same')
    main_graph.subgraph(title_graph)

    for index in range(0, length):
        tmp_graph = Digraph()
        for title in titles:
            tmp_graph.node('%s%d' % (title, index))
        tmp_graph.graph_attr.update(rank='same')
        main_graph.subgraph(tmp_graph)

    return main_graph, all_node

titles = ['a','b','c','d']
g, all_node = draw_flow(titles, 20)
g.node_attr = {'frontsize':'10','shape':'point','color':'grey','label':''}
g.edge_attr = {'arrowhead':'none','style':'filled','color':'grey'}

m = Digraph('event','event')
m.edge_attr = {'style':'filled','frontsize':'8', 'weight':'0','arrowhead':'normal','color':'blue'}
m.edge(all_node['a'][0], all_node['b'][0], label ='req')

g.engine = 'dot'
g.subgraph(m)

g.view()