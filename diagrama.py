import graphviz

# Diagrama de Vista de Desarrollo
dev_graph = graphviz.Digraph('Vista de Desarrollo', format='png')

dev_graph.attr(rankdir='LR', size='8,5')

dev_graph.node('UI', 'Aplicación Móvil (Kotlin/Jetpack Compose)')
dev_graph.node('API', 'Servidor Backend (Node.js/Express)')
dev_graph.node('DB', 'Base de Datos (PostgreSQL)')
dev_graph.node('MAP', 'Servicios de Google Maps API')

dev_graph.edges([('UI', 'API'), ('API', 'DB'), ('UI', 'MAP')])

# Guardar
dev_graph.render('/mnt/data/vista_desarrollo')


# Diagrama de Vista de Despliegue
deploy_graph = graphviz.Digraph('Vista de Despliegue', format='png')

deploy_graph.attr(rankdir='TB', size='8,5')

deploy_graph.node('User', 'Dispositivo Android (Usuario)')
deploy_graph.node('Server', 'Servidor de Aplicaciones (AWS EC2, DigitalOcean)')
deploy_graph.node('Database', 'Base de Datos (PostgreSQL en nube)')

deploy_graph.edge('User', 'Server', label='HTTPS')
deploy_graph.edge('Server', 'Database', label='Red Privada')

# Guardar
dev_graph.render('C:/Users/santi/OneDrive/Documentos/PYTHON/vista_desarrollo', format='pdf', view=True)