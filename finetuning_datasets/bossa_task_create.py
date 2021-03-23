"""
rm no_mnli.csv; for file in *.jsonl; do cat "$file" | jq -sr ".[] | [.genre,.gold_label,.pairID,.promptID,.sentence1,.sentence2,\"$file\"] | @csv" >> no_mnli.csv; done
pbs add_tasks --tasks-file no_mnli.csv
"""
import argparse
import csv
import pandas as pd


def main():
    mnli_en = pd.read_csv(
        "en_mnli.csv",
        names=["genre", "gold_label", "pairID", "promptID", "sentence1", "sentence2", "source"],
        index_col=False,
        dtype={"pairID": str, "promptID": str},
    ).fillna("").drop_duplicates(["pairID", "promptID"], keep=False)
    mnli_en["source"] = mnli_en.source.str.rsplit(".", 1).str.get(0)
    mnli_en_dict = mnli_en.set_index(["promptID", "pairID"]).to_dict(orient="index")

    mnli = pd.read_csv(
        "no_mnli.csv",
        names=["genre", "gold_label", "pairID", "promptID", "sentence1", "sentence2", "source"],
        index_col=False,
        dtype={"pairID": str, "promptID": str},
    ).fillna("").drop_duplicates(["pairID", "promptID"], keep=False)
    mnli["source"] = mnli.source.str.rsplit(".", 1).str.get(0)
    grouper = ["sentence1", "genre", "source", "promptID"]
    mnli_dict = mnli.groupby(grouper).agg(
        lambda rows: rows.to_dict(orient="records")
    ).to_dict()

    rows = []
    for (sentence1, genre, source, prompt_id), values in mnli_dict.items():
        key_dict = {
            'genre': genre,
            'promptID': prompt_id,
            'sentence1': sentence1,
            'source': source,
        }
        dics = {}
        for value_index, value_dict in enumerate(values, 1):
            dic = {}
            for key, value in value_dict.items():
                if key not in grouper:
                    dic[f"{key}_{value_index}"] = value
                if key == "pairID":
                    en_pairs = mnli_en_dict[(prompt_id, value)]
                    dic[f"sentence1_en"] = en_pairs["sentence1"]
                    dic[f"sentence2_{value_index}_en"] = en_pairs["sentence2"]
            dics.update(dic)
        rows.append({**key_dict, **dics})

    mnli_bossa = pd.DataFrame(rows).fillna("")[[
        "genre", "promptID", "sentence1", "sentence1_en",
        "pairID_1", "gold_label_1", "sentence2_1", "sentence2_1_en",
        "pairID_2", "gold_label_2", "sentence2_2", "sentence2_2_en",
        "pairID_3", "gold_label_3", "sentence2_3", "sentence2_3_en",
        "source"
    ]]
    mnli_bossa.to_csv("no_mnli_bossa.csv", index=False, quoting=csv.QUOTE_ALL)
    for source in mnli_bossa.source.unique().tolist():
        mnli_bossa.query(f"source == '{source}'").to_csv(f"no_{source}_bossa.csv", index=False, quoting=csv.QUOTE_ALL)


if __name__ == "__main__":
    # yesno = lambda x: str(x).lower() in {'true', 't', '1', 'yes', 'y'}
    parser = argparse.ArgumentParser(description=f""
    f"Generates CSVs for PyBOSSA tasks on translation checking and correction. "
    f"It needs two files, no_mnli.csv and en_mnli.csv, "
    f"which can be generated for the English and "
    f"Norwegian machine translated versions of the datasets in .jsonl format "
    f"""as follows using 'jq':

    rm no_mnli.csv; for file in norwegian/*.jsonl; do cat "$file" | jq -sr ".[] | [.genre,.gold_label,.pairID,.promptID,.sentence1,.sentence2,\"$file\"] | @csv" >> no_mnli.csv; done
    rm en_mnli.csv; for file in english/*.jsonl; do cat "$file" | jq -sr ".[] | [.genre,.gold_label,.pairID,.promptID,.sentence1,.sentence2,\"$file\"] | @csv" >> en_mnli.csv; done

    It will then create one task CSV per soure as well as one combined.
    """
    f"", formatter_class=argparse.RawTextHelpFormatter)

    args = parser.parse_args()
    main(args)
