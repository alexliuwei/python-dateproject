import  pygal.maps.world
wm = pygal.maps.world.World()
wm.title = 'North, Central, and South America'
wm.add('North America', {'ca':340000 , 'mx':12525220 , 'us':5498855})
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'cn',
'gy', 'pe', 'py', 'sr', 'uy', 've'])
wm.render_to_file('americas.svg')