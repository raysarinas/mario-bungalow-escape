from graph import Graph
import pygame

def generate_graph(surface, screenwidth, screenheight, walls, wall_list):
    graph = Graph
    xrange = (screenwidth - 10) // 25 + 1
    yrange = (screenheight - 10) // 25 + 1
    print(xrange, yrange)
    print(walls)
    vertices = []

    for i in range(1, xrange):
        for j in range(1, yrange):
            vertices.append([25 * i, 25 * j])

    print(vertices)
    print(len(vertices))

    # THIS MIGHT BE THE BETTER WAY TO GETTING THE VALID VERTICES? IDK
    rects = []
    '''
    for wall in wall_list:
        for i in range(len(vertices)):
            if wall.rect.collidepoint(vertices[i]):
                continue
            else:
                validverts[i] = vertices[i]
                rects.append(pygame.Rect(vertices[i][0], vertices[i][1], 1, 1))
                # pygame.draw.rect(surface, pygame.Color('red'), rect)
    '''


    vertdict = {}

    for i in range(len(vertices)):
        vertdict[i] = vertices[i]

    #print(vertdict)

    topleft_bounds = []
    bottomright_bounds = []

    for k in range(len(walls)):
        startx, starty = walls[k][0], walls[k][1] # top left coords
        width, height = walls[k][2], walls[k][3] # size of rects
        xbound, ybound = startx+width, starty+height # bottom left coords
        topleft_bounds.append([startx, starty])
        bottomright_bounds.append([xbound, ybound])

    #print(topleft_bounds)
    #print(bottomright_bounds)

    valid = []

# something along these lines should implement algorithm that
# only adds valid vertices

    invalidverts = {}
    invalid = []

# NEED TO FIX THIS???
    for v in vertices:
        for i in range(len(walls)):
            if v[0] in range(topleft_bounds[i][0], bottomright_bounds[i][0]):
                if v[1] in range(topleft_bounds[i][1], bottomright_bounds[i][1]):
                    invalidverts[i] = v # SOMETHING WRONG WITH IDENTIFIERS HERE
                    # YEAH INDEXING IS JUST WRONG HERE
                    invalid.append(v)
                    rects.append(pygame.Rect(v[0], v[1], 1, 1))

    print(invalid)
    print(len(invalid))
    print(invalidverts)
    print(len(invalidverts))


    for key in vertdict.keys():
        if key in invalidverts.keys():
            print(invalidverts[key])

    '''
    for i in range(len(vertdict.values())):
        if i in invalid:
            # somehow delete the item with the value but like delete key?
    print(len(vertdict))
    '''

    for i in range(len(vertdict.keys())):
        if i in invalidverts.keys():
            print(i, vertdict[i])
            del vertdict[i]
    print(len(vertdict))

    # OK SO DELETING THE RIGHT VERTICES BUT STILL NOT DRAWING PROPERLY??

    for v in vertdict.values():
        pass #rects.append(pygame.Rect(v[0], v[1], 2, 2))

    return vertdict, rects #invalidverts, rects


    '''#if vertices[v][0] in range(topleft_bounds[0][0], bottomright_bounds[0][0]):
        if not True:    # ^^^^ THIS ISNT RIGHT I THINK
            pass
        else:
            print(v[0])
            valid.append(v)'''




#generate_graph(600, 400)
