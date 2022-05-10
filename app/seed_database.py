import psycopg2
from psycopg2 import Error
from importProviders import import_providers


def seed():
    #open cursor to perform operations
    try: 
        conn = psycopg2.connect(host="localhost", database="postgres", user="root", password="root", port="5432")
        cur = conn.cursor()

    #get list of providers
        providers = import_providers()

        cur.execute("delete from provider;")
        conn.commit()

        for provider in providers:
            providerCols = [provider.id, provider.first_name, provider.last_name, provider.sex, provider.birth_date, provider.rating, provider.primary_skills, provider.secondary_skill, provider.company, provider.active, provider.country, provider.language]
            cur.execute("INSERT INTO provider (id, first_name, last_name, sex, birth_date, rating, primary_skills, secondary_skill, company, active, country, language) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", providerCols)

            #primarySkills = map(lambda skill: [provider.id, skill], provider.primary_skills)
            #cur.executemany("INSERT INTO primaryskill (provider_id, skill) VALUES (%s, %s)", primarySkills)

            #secondarySkills = map(lambda skill: [provider.id, skill], provider.secondary_skills)
            #cur.executemany("INSERT INTO secondaryskill (provider_id, skill) VALUES(%s, %s)", secondarySkills)

        conn.commit()

    except(Exception, Error) as error:
        print("Error", error)

    finally:
        cur.close()
        conn.close()


