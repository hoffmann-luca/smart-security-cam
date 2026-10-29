package com.example.home.securitycam;


import android.os.AsyncTask;

import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.Socket;

/**
 * Created by Home on 07.10.2017.
 */

public class Connect extends AsyncTask<String, Void, Void> {
    private  Exception exception;
    public static Socket socket;
    protected Void doInBackground(String... params){
        try{
            try{
                socket = new Socket(params[0], 64932);
                PrintWriter outToServer = new PrintWriter(new OutputStreamWriter(socket.getOutputStream()));
                for (String param:params) {
                    if(param.contains("192.")){
                        continue;
                    }else{
                        outToServer.print(param+"\n");
                    }
                }
                outToServer.flush();
                socket.close();
            }catch (IOException e){
                e.printStackTrace();
            }
        }catch (Exception e){
            this.exception = e;
            return null;
        }
        return null;
    }
}
