#include <vision/vision.h>

int main(int argc, char** argv) {
    d3t12::ColorJSONLoader loader;
    loader.setFile("colors.json");
    loader.loadJSON();

    d3t12::ColorPalette palette;
    loader.fillPalette(palette);
    d3t12::ColorFilter colorFilter(palette.getColor(argv[2]));
    
    cv::Mat input = cv::imread(argv[1]), resizedInput;
    cv::resize(input, resizedInput, cv::Size(input.size().width*(atof(argv[3])), input.size().height*(atof(argv[3]))) , 0, 0, cv::INTER_LANCZOS4);

    cv::Mat workingSquaresMatrix = resizedInput.clone();
    cv::Mat outputSquaresMatrix = resizedInput.clone(), 
    colorsMask;

    colorFilter.filter(colorsMask, resizedInput);

    d3t12::SquareFilter squareFilter;
    squareFilter.find_squares(workingSquaresMatrix);
    squareFilter.drawSquares(outputSquaresMatrix);

    cv::Mat finalMatrix;
    outputSquaresMatrix.copyTo(finalMatrix/*, colorsMask*/);
    
    cv::imshow("resizedInput", resizedInput);
    cv::imshow("output", finalMatrix);
    cv::waitKey(0);

    return 0;
}