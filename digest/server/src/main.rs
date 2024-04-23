// #![deny(warnings)]

use std::convert::Infallible;
use std::str::FromStr;
use std::time::Duration;
use warp::Filter;
use rust_bert::pipelines::question_answering::{QaInput, QuestionAnsweringModel};

#[tokio::main]
async fn main() {

    let question = warp::path::param()
        .and_then(answer_question);

    warp::serve(question).run(([0, 0, 0, 0], 5000)).await;
}

async fn sleepy(Seconds(seconds): Seconds) -> Result<impl warp::Reply, Infallible> {
    tokio::time::sleep(Duration::from_secs(seconds)).await;
    Ok(format!("I waited {} seconds!", seconds))
}

async fn answer_question(question: String) -> Result<impl warp::Reply, warp::Rejection> {

    print!("Got question: {}", question);
    let qa_model = QuestionAnsweringModel::new(Default::default()).unwrap();

    let question = String::from(question);
    let context = String::from("A terra é redonda. Há lixo no chão. O Batman é português.");

    let answers = qa_model.predict(&[QaInput { question, context }], 1, 32);

    Ok(format!("Ans: {}", answers[0][0].answer))
}

/// A newtype to enforce our maximum allowed seconds.
struct Seconds(u64);

impl FromStr for Seconds {
    type Err = ();
    fn from_str(src: &str) -> Result<Self, Self::Err> {
        src.parse::<u64>().map_err(|_| ()).and_then(|num| {
            if num <= 5 {
                Ok(Seconds(num))
            } else {
                Err(())
            }
        })
    }
}
