# project path should not end with '/'
from project_scheme_graph import ProjectSchemeGraph
# ploting graph with saving
scheme = ProjectSchemeGraph('project_path')
scheme.plot_graph(save=True)


# Saving edges in .csv format
scheme.save_edges()


# Saving edges in .xlsx format
scheme.save_edges(save_format='xlsx')


# Saving edges in .json format
scheme.save_edges(save_format='json')

