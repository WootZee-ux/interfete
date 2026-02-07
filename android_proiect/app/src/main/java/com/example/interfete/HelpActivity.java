package com.example.interfete;

import android.os.Bundle;
import android.widget.Button;

public class HelpActivity extends BaseActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_help);
        setupToolbar(getString(R.string.help_title));

        Button backToMenuButton = findViewById(R.id.backToMenuButton);
        backToMenuButton.setOnClickListener(view -> finish());
    }
}
