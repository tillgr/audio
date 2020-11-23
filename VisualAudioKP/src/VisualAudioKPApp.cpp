#include "cinder/app/App.h"
#include "cinder/app/RendererGl.h"
#include "cinder/gl/gl.h"

using namespace ci;
using namespace ci::app;
using namespace std;

class VisualAudioKPApp : public App {
  public:
	void setup() override;
	void mouseDown( MouseEvent event ) override;
	void update() override;
	void draw() override;
};

void VisualAudioKPApp::setup()
{
}

void VisualAudioKPApp::mouseDown( MouseEvent event )
{
}

void VisualAudioKPApp::update()
{
}

void VisualAudioKPApp::draw()
{
	gl::clear( Color( 0, 0, 0 ) ); 
}

CINDER_APP( VisualAudioKPApp, RendererGl )
