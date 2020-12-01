#include "cinder/app/App.h"
#include "cinder/gl/gl.h"
#include "cinder/app/RendererGl.h"

#include "cinder/audio/audio.h"

#include "essentiamath.h"
#include "algorithmfactory.h"
#include "essentia.h"
#include "pool.h"
#include "algorithmfactory.h"

#include "Resources.h"

using namespace ci;
using namespace ci::app;

using namespace essentia;
using namespace essentia::standard;

class AudioKPApp : public App {
  public:
	void setup() override;
	void mouseDown( MouseEvent event ) override;
	void update() override;
	void draw() override;
    
    audio::GainNodeRef                mGain;
    audio::BufferPlayerNodeRef        mBufferPlayerNode;
};

void AudioKPApp::setup()
{
    auto ctx = audio::Context::master();
    audio::SourceFileRef sourceFile = audio::load( loadResource( SAMPLE_SOUND_WAV ), ctx->getSampleRate() );
    
    audio::BufferRef buffer = sourceFile->loadBuffer();
    mBufferPlayerNode = ctx->makeNode( new audio::BufferPlayerNode( buffer ) );

    // add a Gain to reduce the volume
    mGain = ctx->makeNode( new audio::GainNode( 0.9f ) );

    // connect and enable the Context
    mBufferPlayerNode >> mGain >> ctx->getOutput();
    ctx->enable();
    
    
    //Essentia stuff

    
    essentia::init();
    Pool pool;
    
    AlgorithmFactory& factory = standard::AlgorithmFactory::instance();
    Algorithm* centroidAlgo = factory.create("SpectralCentroidTime");
    
    Real myCentroid;            // the variable containing the resulting centroid

    // point the input/output of the algorithm to their respective variable
    centroidAlgo->input("array").set(buffer);
    centroidAlgo->output("centroid").set(myCentroid);

    // only now can you call compute()
    centroidAlgo->compute();

//    Algorithm* audio = factory.create("MonoLoader",
//                                      "filename", audioFilename,
//                                      "sampleRate", ctx->getSampleRate() );
//
//    Algorithm* fc    = factory.create("FrameCutter",
//                                      "frameSize", frameSize,
//                                      "hopSize", hopSize);
//
//    Algorithm* w     = factory.create("Windowing",
//                                      "type", "blackmanharris62");
//
//    Algorithm* spec  = factory.create("Spectrum");
//    Algorithm* mfcc  = factory.create("MFCC");




    /////////// CONNECTING THE ALGORITHMS ////////////////
    std::cout << "-------- connecting algos ---------" << std::endl;

    // Audio -> FrameCutter
    std::vector<Real> audioBuffer;

    audio->output("audio").set(audioBuffer);
    fc->input("signal").set(audioBuffer);

    // FrameCutter -> Windowing -> Spectrum
    std::vector<Real> frame, windowedFrame;

    fc->output("frame").set(frame);
    w->input("frame").set(frame);

    w->output("frame").set(windowedFrame);
    spec->input("frame").set(windowedFrame);

    // Spectrum -> MFCC
    std::vector<Real> spectrum, mfccCoeffs, mfccBands;

    spec->output("spectrum").set(spectrum);
    mfcc->input("spectrum").set(spectrum);

    mfcc->output("bands").set(mfccBands);
    mfcc->output("mfcc").set(mfccCoeffs);
}

void AudioKPApp::mouseDown( MouseEvent event )
{
    mBufferPlayerNode->start();
}

void AudioKPApp::update()
{
}

void AudioKPApp::draw()
{
	gl::clear( Color( 0, 0, 0 ) ); 
}

CINDER_APP( AudioKPApp, RendererGl )
