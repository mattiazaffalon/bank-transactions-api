terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "4.51.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_sql_database_instance" "bank-transactions-api-db" {
  name             = "bank-transactions-api-db"
  database_version = "MYSQL_8_0_26"
  region           = "europe-west6"

  settings {
    tier = "db-custom-1-3840"
  }
}

resource "google_sql_user" "users" {
  name     = var.db_user
  instance = google_sql_database_instance.bank-transactions-api-db.name
  password = var.db_password
}

resource "google_sql_database" "database" {
  name     = "bank_transactions"
  instance = google_sql_database_instance.bank-transactions-api-db.name
}

resource "google_secret_manager_secret" "bank-transactions-db-user-password" {
  secret_id = "bank-transactions-user-password"

  replication {
    user_managed {
      replicas {
        location = var.region
      }
    }
  }
}

module "cloud_run" {
  source  = "GoogleCloudPlatform/cloud-run/google"
  version = "~> 0.2.0"

  # Required variables
  service_name           = "bank-transactions-api"
  project_id             = var.project_id
  location               = "europe-west6"
  image                  = "gcr.io/cloudrun/hello"

  env_vars = [
    {
      "name": "DB_HOST",
      "value": "34.65.237.173"
    },
    {
      "name": "DB_PORT",
      "value": "3306"
    },
    {
      "name": "DB_USER",
      "value": var.db_user
    },
    {
      "name": "DB_PASSWORD",
      "value": var.db_password
    },
    {
      "name" : "DB_NAME",
      "value" : google_sql_database.database.name
    },
    {
      "name" : "DB_DATABASE",
      "value" : "bank_transactions"
    },
    {
      "name"  = "INSTANCE_CONNECTION_NAME"
      "value" = google_sql_database_instance.bank-transactions-api-db.connection_name
    },
    {
      "name" : "RUN_ENVIRONMENT",
      "value" : "gcp"
    }
  ]
}
