import pygame as pg
import sys

f = 1800

def project(point: pg.Vector3) -> pg.Vector2:
    dims = pg.display.get_surface().get_size()
    midx = dims[0]/2
    midy = dims[1]/2
    
    r_vec = pg.Vector2()
    r_vec.x = midx - (midx-point.x) * f/(f+point.z)
    r_vec.y = midy - (midy-point.y) * f/(f+point.z)
    # r_vec.x = midx - (midx-point.x)
    # r_vec.y = midy - (midy-point.y)
    
    return r_vec

def draw_shape(points: list[pg.Vector3], edges: tuple[tuple[int, int], ...], cam_pos: pg.Vector3, cam_pitch: float, cam_yaw: float) -> None:
    cam_points  = [p.rotate_y(-cam_yaw) for p in points]
    cam_points  = [p.rotate_x(cam_pitch) for p in cam_points]
    cam_points  = [p + cam_pos for p in cam_points]
    proj_points = [project(p)  for p in cam_points]
    
    
    for edge in edges:
        pg.draw.line(
            pg.display.get_surface(),
            (255, 255, 255),
            proj_points[edge[0]],
            proj_points[edge[1]]
        )



def main():
    pg.init()
    pg.display.set_mode((800, 600))
    
    points = [
        pg.Vector3(0,   0,   0), 
        pg.Vector3(100, 0,   0),
        pg.Vector3(100, 100, 0),
        pg.Vector3(0,   100, 0),
        pg.Vector3(0,   0,   100), 
        pg.Vector3(100, 0,   100),
        pg.Vector3(100, 100, 100),
        pg.Vector3(0,   100, 100)
    ]
    edges = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], [7, 4], [0, 4], [1, 5], [2, 6], [3, 7]]
    
    p, y = 0, 0
    
    clock = pg.time.Clock()
    while True:
        clock.tick(60)
        for ev in pg.event.get():
            if ev.type == pg.KEYDOWN:
                match ev.key:
                    case pg.K_ESCAPE:
                        pg.event.post(pg.event.Event(pg.QUIT))
            if ev.type == pg.QUIT:
                pg.quit()
                sys.exit()
        mid = pg.Vector2(800, 600)/2
        delta = pg.mouse.get_pos() - mid
        pg.mouse.set_pos(mid)
        
        y += delta[0]
        p += delta[1]
        
        print(delta)
        
        pg.display.get_surface().fill('black')
        draw_shape(points, edges, (0,0,0), p, y)
        pg.display.update()
        


if __name__ == '__main__':
    main()