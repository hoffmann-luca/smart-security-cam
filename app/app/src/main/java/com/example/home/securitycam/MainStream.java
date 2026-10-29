package com.example.home.securitycam;

import android.net.Uri;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.webkit.WebView;
import android.widget.Button;
import android.widget.MediaController;
import android.widget.VideoView;

public class MainStream extends AppCompatActivity {

    public Button back;
    //public VideoView videoView;
    public WebView view;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_stream);

        back = (Button)findViewById(R.id.buttonBack);
       // videoView = (VideoView)findViewById(R.id.videoView);
        view = (WebView)findViewById(R.id.webview) ;

        view.loadUrl("http://" + MainActivity.IpSaver.getText().toString() + ":5000");

       // MediaController mediaController = new MediaController(this);
        //mediaController.setAnchorView(videoView);
        //Uri uri = Uri.parse("http://" + MainActivity.IpSaver.getText().toString() + ":5000");
        //videoView.setMediaController(mediaController);
        //videoView.setVideoURI(uri);
        //videoView.start();

        back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //videoView.stopPlayback();
                view.destroy();
                finish();
            }
        });
    }
}
