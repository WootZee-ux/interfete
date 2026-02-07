package com.example.interfete;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;

public class DataManagementActivity extends BaseActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_data_management);
        setupToolbar(getString(R.string.data_management_title));

        Button saveItemButton = findViewById(R.id.saveItemButton);
        Button backToMenuButton = findViewById(R.id.backToMenuButton);

        saveItemButton.setOnClickListener(view -> {
            EditText feedback = findViewById(R.id.itemValueInput);
            feedback.setError("Datele au fost salvate local.");
        });

        backToMenuButton.setOnClickListener(view -> finish());
    }
}
