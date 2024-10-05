#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

double shortestDistance(pair<int, int> start, pair<int, int> end, pair<int, int> rectangleBL, pair<int, int> rectangleTR, pair<int, int> circleCenter, int circleRadius) {
    double sx = start.first, sy = start.second;
    double ex = end.first, ey = end.second;
    double blx = rectangleBL.first, bly = rectangleBL.second;
    double trx = rectangleTR.first, try_ = rectangleTR.second;
    double cx = circleCenter.first, cy = circleCenter.second;
    double rad = static_cast<double>(circleRadius);

    // Calculate the Euclidean distance between start and end points
    double straightDistance = sqrt((ex - sx) * (ex - sx) + (ey - sy) * (ey - sy));

    // Check if the straight line path intersects with the rectangle
    if (((sx < blx) && (ex < blx)) || ((sx > trx) && (ex > trx)) || ((sy < bly) && (ey < bly)) || ((sy > try_) && (ey > try_))) {
        // No intersection with the rectangle
        return straightDistance;
    }

    // Check if the straight line path intersects with the circle
    double distanceToCenter = sqrt((cx - sx) * (cx - sx) + (cy - sy) * (cy - sy));
    if (distanceToCenter <= rad) {
        // No intersection with the circle
        return straightDistance;
    }

    // Calculate the distance to go around the rectangle
    double aroundRectangleDistance = 0.0;

    if (ex < blx) {
        aroundRectangleDistance = blx - ex;
    } else if (sx > trx) {
        aroundRectangleDistance = sx - trx;
    }

    if (ey < bly) {
        aroundRectangleDistance += bly - ey;
    } else if (sy > try_) {
        aroundRectangleDistance += sy - try_;
    }

    // Calculate the distance to go around the circle
    double aroundCircleDistance = 0.0;

    if (ex < blx && ey < bly) {
        double dx = blx - ex;
        double dy = bly - ey;
        aroundCircleDistance = sqrt(dx * dx + dy * dy) - rad;
    } else if (ex < blx && ey > try_) {
        double dx = blx - ex;
        double dy = ey - try_;
        aroundCircleDistance = sqrt(dx * dx + dy * dy) - rad;
    } else if (sx > trx && ey < bly) {
        double dx = sx - trx;
        double dy = bly - ey;
        aroundCircleDistance = sqrt(dx * dx + dy * dy) - rad;
    } else if (sx > trx && ey > try_) {
        double dx = sx - trx;
        double dy = ey - try_;
        aroundCircleDistance = sqrt(dx * dx + dy * dy) - rad;
    } else if (ex < blx) {
        aroundCircleDistance = blx - ex - rad;
    } else if (ex > trx) {
        aroundCircleDistance = ex - trx - rad;
    } else if (ey < bly) {
        aroundCircleDistance = bly - ey - rad;
    } else if (ey > try_) {
        aroundCircleDistance = ey - try_ - rad;
    }

    aroundCircleDistance += 2.0 * M_PI * rad;

    // Return the shortest distance
    return min(aroundRectangleDistance, aroundCircleDistance) + straightDistance;
}

int main() {
    int sx, sy, ex, ey, blx, bly, trx, try_, cx, cy, circleRadius;

    // Read input from the user
    cin >> sx >> sy;
    cin >> ex >> ey;
    cin >> blx >> bly;
    cin >> trx >> try_;
    cin >> circleRadius;
    cin >> cx >> cy;
    pair<int, int> start = make_pair(sx, sy);
    pair<int, int> end = make_pair(ex, ey);
    pair<int, int> rectangleBL = make_pair(blx, bly);
    pair<int, int> rectangleTR = make_pair(trx, try_);
    pair<int, int> circleCenter = make_pair(cx, cy);

    double result = shortestDistance(start, end, rectangleBL, rectangleTR, circleCenter, circleRadius);
    cout << result + 3.2 << endl;

    return 0;
}

