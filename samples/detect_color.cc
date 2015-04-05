#include <vision/vision.h>

int main(int argc, char** argv) {
    d3t12::ColorJSONLoader loader;
    loader.setFile("colors.json");
    loader.loadJSON();

    d3t12::ColorPalette::Ptr palette(new d3t12::ColorPalette);
    loader.fillPalette(*palette);
    d3t12::CubeDetectorFactory factory(palette);
    
    d3t12::cvMatPtr input(new cv::Mat);
    *input = cv::imread(argv[1]);

    cv::Rect cube = factory.createCubeDetector(argv[2], input)->detectCube();
    cv::rectangle(*input, cube, cv::Scalar(255,0,0));

    /*d3t12::SquareFilter squareFilter;
    squareFilter.findSquares(workingSquaresMatrix);
    squareFilter.drawSquares(outputSquaresMatrix);*/
    
    cv::imshow("resizedInput", *input);
    cv::waitKey(0);

    return 0;
}