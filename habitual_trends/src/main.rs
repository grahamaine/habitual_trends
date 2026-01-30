use log::info;

fn main() {
    // This initializes the logger
    env_logger::init();

    info!("The logger is now working!");
}